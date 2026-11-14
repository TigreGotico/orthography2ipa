#!/usr/bin/env python3
"""STE + slop linter for the ste-writing skill.

Usage:
  ste_lint.py [--mode strict|flavored] [--nav] [file ...]   # or pipe text on stdin
--nav also checks the doc-set footer convention (index files exempt).
Exit code 1 when the text fails its mode's threshold.
"""
import re, sys, json, glob, os

MARKETING = ["seamless","seamlessly","robust","powerful","cutting-edge","effortless","effortlessly",
    "world-class","next-generation","revolutionary","blazing","lightning-fast","elegant","delightful",
    "turnkey","best-in-class","state-of-the-art","game-changing","first-class","battle-tested",
    "enterprise-grade","supercharge","unlock","unleash","empower","empowers"]
BANNED = ["commence","commences","initiate","initiates",
    "utilize","utilizes","utilizing","leverage","leverages","leveraging","facilitate","facilitates",
    "prior to","subsequent to","additionally","furthermore","moreover",
    "aforementioned","henceforth","therein","whilst","amongst","myriad","plethora",
    "in order to","in the event that","due to the fact that"]
SLOP = ["delve","delves","delving","crucial","pivotal","tapestry","testament to","landscape of",
    "in today's","not just a","not merely","whether you're","whether you are",
    "happy coding","you're all set","that's it!","dive into","dives into","diving into",
    "it is important to note","it should be noted","it is worth noting","game changer",
    "the beauty of","at its core,","seamlessly integrates"]
PHRASAL = ["spin up","spin down","reach out","kick off","kicks off","roll out","rolls out",
    "tear down","ramp up","circle back","drill down","spun up","reaching out"]
BE = r"(?:am|is|are|was|were|be|been|being)"
PP_IRREG = r"(?:done|made|sent|built|kept|held|written|shown|given|taken|found|seen|known|thrown|drawn)"

def strip_code(t):
    t = re.sub(r"```.*?```", " ", t, flags=re.S)
    t = re.sub(r"`[^`]*`", " ", t)
    t = re.sub(r"^\s{4,}\S.*$", " ", t, flags=re.M)  # indented code blocks
    t = re.sub(r"https?://\S+", " ", t)
    return t

def sentences(text):
    out = []
    for line in text.split("\n"):
        s = line.strip()
        if not s: continue
        s = re.sub(r"^\s*#{1,6}\s*", "", s)
        s = re.sub(r"^\s*(?:[-*+]|\d+[.)])\s+", "", s)
        if not s: continue
        for p in re.split(r"(?<=[.!?:])\s+(?=[A-Z0-9\"'\-])", s):
            p = p.strip()
            if p: out.append(p)
    return out

def wc(s):
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'\-/]*", s))

def count_ci(text, phrases):
    hits = []
    low = text.lower()
    for ph in phrases:
        hits += [ph] * len(re.findall(r"(?<![a-z])" + re.escape(ph) + r"(?![a-z])", low))
    return len(hits), hits

def lint(text, mode="flavored"):
    raw = text
    text = strip_code(text)
    sents = sentences(text)
    words = sum(wc(s) for s in sents) or 1
    v = {}
    longs = [(wc(s), s) for s in sents if wc(s) > (20 if mode == "strict" else 25)]
    v["long_sentence"] = len(longs)
    v["semicolon"] = text.count(";")
    v["em_dash"] = raw.count("—") + raw.count("–")
    if mode == "strict":
        v["contraction"] = len(re.findall(r"\b\w+['’](?:t|re|ve|ll|d|m)\b", text))
    v["passive_known_actor"] = len(re.findall(rf"\b{BE}\s+(?:\w+ed|{PP_IRREG})\s+by\s+(?:the|a|an|this)\b", text, re.I))
    v["nominalization"] = len(re.findall(r"\b(?:perform(?:s|ed)?|carry out|carries out|make use of|makes use of)\s+(?:an?|the)\s+\w+", text, re.I))
    v["phrasal_verb"], _ = count_ci(text, PHRASAL)
    v["banned_word"], bh = count_ci(text, BANNED)
    v["marketing_adjective"], mh = count_ci(text, MARKETING)
    v["SLOP"], sh = count_ci(text, SLOP)
    v["emoji"] = len(re.findall(r"[\U0001F000-\U0001FAFF✀-➿☀-⛿]", raw))
    v["rule_of_three"] = len(re.findall(r"\b\w+, \w+, and \w+\b(?=[.!\n])", text))
    nocode = re.sub(r"```.*?```", " ", raw, flags=re.S)
    nocode = re.sub(r"`[^`]*`", " ", nocode)
    v["bare_url"] = len(re.findall(r"(?<![(<])https?://\S+", nocode))
    v["branch_permalink"] = len(re.findall(r"github\.com/[\w.-]+/[\w.-]+/(?:blob|tree)/(?:master|main|dev)/\S+#L\d", nocode))
    paras = [p for p in re.split(r"\n\s*\n", raw) if p.strip()]
    v["long_paragraph"] = sum(1 for p in paras if len(sentences(strip_code(p))) > 6)
    total = sum(v.values())
    per100 = round(total * 100.0 / words, 2)
    if mode == "strict":
        passed = total == 0
    else:
        passed = per100 < 2.0 and v["SLOP"] == 0 and v["marketing_adjective"] == 0
    return {"mode": mode, "words": words, "sentences": len(sents),
            "violations": {k: n for k, n in v.items() if n},
            "total": total, "per100w": per100, "pass": passed,
            "worst_sentences": [s for _, s in sorted(longs, reverse=True)[:3]],
            "hits": list(dict.fromkeys(bh + mh + sh))[:10]}

NAV_RE = re.compile(
    r"^(?:\[← [^\]]+\]\([^)]+\) · )?\[Home\]\([^)]+\)(?: · \[[^\]]+ →\]\([^)]+\))?$")

def nav_check(path, raw):
    """Return violation count for the footer convention. Index pages are exempt."""
    if os.path.basename(path).lower() in ("readme.md", "index.md"):
        return 0
    lines = [l.strip() for l in raw.rstrip().split("\n") if l.strip()]
    if len(lines) < 2 or lines[-2] != "---" or not NAV_RE.match(lines[-1]):
        return 1
    v = 0
    for target in re.findall(r"\]\(([^)#]+)", lines[-1]):
        if target.startswith("http"):
            v += 1  # footer links must be relative
        elif not os.path.exists(os.path.join(os.path.dirname(path) or ".", target)):
            v += 1  # footer link target missing
    return v

if __name__ == "__main__":
    argv = sys.argv[1:]
    mode = "flavored"
    nav = "--nav" in argv
    if nav: argv.remove("--nav")
    if "--mode" in argv:
        i = argv.index("--mode"); mode = argv[i + 1]; del argv[i:i + 2]
    files = []
    for f in argv:
        files += sorted(glob.glob(f)) if any(c in f for c in "*?[") else [f]
    fail = False
    if not files:
        r = lint(sys.stdin.read(), mode)
        print(json.dumps(r, indent=2)); fail = not r["pass"]
    else:
        for f in files:
            with open(f) as fh: raw = fh.read()
            r = lint(raw, mode)
            if nav:
                n = nav_check(f, raw)
                if n:
                    r["violations"]["nav_footer"] = n
                    r["total"] += n; r["pass"] = False
            flag = "PASS" if r["pass"] else "FAIL"
            print(f"{os.path.basename(f):32} {flag} words={r['words']:4d} total={r['total']:3d} "
                  f"per100w={r['per100w']:6.2f} " + (f"hits={','.join(r['hits'][:4])}" if r['hits'] else ""))
            fail = fail or not r["pass"]
    sys.exit(1 if fail else 0)
