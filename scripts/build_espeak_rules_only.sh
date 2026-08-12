#!/usr/bin/env bash
# Builds a "rules-only" espeak-ng compiled data set for scripts/compare_systems.py's
# `espeak_rules` column: the same dictsource/<lang>_rules (letter-to-sound rules)
# espeak-ng normally ships, compiled with the dictsource/<lang>_list /
# _listx / _extra word-EXCEPTION files emptied first.
#
# This automates building GPL espeak-ng locally to derive a comparison data
# set. It clones and builds espeak-ng from source into a scratch work dir and
# writes the compiled dictionaries to an output dir — nothing GPL is fetched,
# built, or written anywhere under this repository's tree, and this script
# ships no espeak-ng source or data itself.
#
# Usage:
#   scripts/build_espeak_rules_only.sh [lang ...]
#   scripts/build_espeak_rules_only.sh                # defaults below
#   scripts/build_espeak_rules_only.sh en fr de nl ca sv eu
#
# Env vars:
#   ESPEAK_RULES_WORK       scratch dir for the espeak-ng clone/build
#                           (default: a fresh mktemp -d)
#   ESPEAK_RULES_ONLY_DIR   output dir for the compiled rules-only data
#                           (default: ./.espeak_rules_only, gitignored)
#
# Then point compare_systems.py at the output:
#   ESPEAK_RULES_DATA_PATH=$(pwd)/.espeak_rules_only \
#       PYTHONPATH=$PWD python scripts/compare_systems.py --scoreboard
#
# Requires: git, and a C build toolchain (autoconf/automake/libtool/
# pkg-config + the espeak-ng build deps — see espeak-ng's own
# docs/building.md for platform-specific package names).
#
# Version pin: cloned/built at the ``1.52.0`` tag (not the default
# branch). Upstream espeak-ng removed ``autogen.sh``/autotools from
# master in favor of a CMake-only build, so an unpinned ``--depth 1``
# clone of the default branch breaks this script's autotools build step
# outright. ``1.52.0`` still ships ``autogen.sh`` and is the exact
# version every published `espeak_rules`/`espeak-rules-only` number on
# this comparison board was measured against (see
# ``scripts/compare_systems.py``'s comparison board) — pinning keeps
# those numbers reproducible AND keeps the build working. Override with
# ``ESPEAK_RULES_TAG`` if a different pinned version is ever needed
# (re-measure the board after changing it — a different espeak-ng
# version is not a drop-in replacement for comparison purposes).
set -euo pipefail

LANGS=("$@")
if [ "${#LANGS[@]}" -eq 0 ]; then
    LANGS=(en fr de nl ca sv eu)
fi

TAG="${ESPEAK_RULES_TAG:-1.52.0}"
WORK="${ESPEAK_RULES_WORK:-$(mktemp -d -t espeak-rules-only.XXXXXX)}"
OUT="${ESPEAK_RULES_ONLY_DIR:-$(pwd)/.espeak_rules_only}"
REPO="$WORK/espeak-ng"

echo "work dir:   $WORK"
echo "output dir: $OUT"
echo "languages:  ${LANGS[*]}"
echo "espeak-ng tag: $TAG"

if [ ! -d "$REPO" ]; then
    echo "cloning espeak-ng $TAG (GPL, scratch-only, never committed)..."
    git clone --depth 1 --branch "$TAG" \
        https://github.com/espeak-ng/espeak-ng.git "$REPO"
else
    checked_out="$(git -C "$REPO" describe --tags --exact-match 2>/dev/null || echo unknown)"
    if [ "$checked_out" != "$TAG" ]; then
        echo "warning: reusing existing checkout at $REPO, which is at" \
             "'$checked_out', not the pinned '$TAG' — delete \$ESPEAK_RULES_WORK" \
             "and re-run to rebuild against the pinned tag." >&2
    fi
fi

BIN="$REPO/src/espeak-ng"
if [ ! -x "$BIN" ]; then
    [ -x "$REPO/autogen.sh" ] || {
        echo "error: $TAG has no autogen.sh (upstream master is" \
             "CMake-only); use a tag <= 1.52.0" >&2
        exit 1
    }
    echo "building espeak-ng..."
    (
        cd "$REPO"
        ./autogen.sh
        ./configure --prefix="$WORK/install"
        make -j"$(nproc)"
    )
fi

if [ ! -x "$BIN" ]; then
    echo "error: espeak-ng build did not produce $BIN" >&2
    exit 1
fi

echo "stripping word-exception lists (keeping *_rules) for: ${LANGS[*]}"
for lang in "${LANGS[@]}"; do
    for suffix in list listx extra; do
        f="$REPO/dictsource/${lang}_${suffix}"
        if [ -f "$f" ]; then
            n=$(wc -l < "$f")
            echo "  emptying $f ($n lines)"
            : > "$f"
        fi
    done
done

rm -rf "$OUT"
mkdir -p "$OUT"
cp -r "$REPO/espeak-ng-data/." "$OUT/"

echo "recompiling stripped dictionaries..."
(
    cd "$REPO/dictsource"
    for lang in "${LANGS[@]}"; do
        echo "  --compile=$lang"
        "$BIN" --compile="$lang" --path="$OUT"
    done
)

echo
echo "done. Rules-only espeak-ng data written to: $OUT"
echo "Run the comparison with:"
echo "  ESPEAK_RULES_DATA_PATH=$OUT PYTHONPATH=\$PWD python scripts/compare_systems.py --scoreboard"
