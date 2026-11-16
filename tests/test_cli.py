import os
import subprocess
import sys

import pytest


def test_family_filter_matches_any_step_of_the_classification_path(capsys):
    """`family` is a Glottolog path ("Indo-European > Romance"). Filtering must
    accept the branch ("Romance") as well as the stock it sits in
    ("Indo-European", which selects every family beneath it), so normalising the
    field to a path does not break the short filter people actually type."""
    import pytest
    from orthography2ipa.cli import main

    for arg in ("Romance", "romance"):
        main(["list", "--family", arg])
        out = capsys.readouterr().out
        assert "Indo-European > Italic > Romance" in out
        assert "pt-PT" in out

    # The stock selects every family beneath it, not just an exact key.
    main(["list", "--family", "Indo-European"])
    out = capsys.readouterr().out
    assert "Indo-European > Italic > Romance" in out
    assert "Indo-European > Armenic" in out

    # An unknown family is still an error.
    with pytest.raises(SystemExit) as exc:
        main(["list", "--family", "Klingon"])
    assert exc.value.code == 1


@pytest.mark.parametrize("argv", [
    ["list"],
    ["list", "--families"],
    ["info", "pt-PT", "--json"],
    ["--version"],
    ["--help"],
], ids=" ".join)
def test_a_closed_pipe_ends_the_command_quietly(argv):
    """`orthography2ipa list | head` closes the pipe before the command is done.

    The read end is closed before the command starts, so every write fails, the
    same as the last write after `head` exits. The command must exit with
    status 1 and write nothing to stderr: no traceback, no "Exception ignored"
    from the flush at interpreter exit.
    """
    read_end, write_end = os.pipe()
    os.close(read_end)
    try:
        proc = subprocess.run(
            [sys.executable, "-m", "orthography2ipa.cli", *argv],
            stdout=write_end, stderr=subprocess.PIPE, timeout=120)
    finally:
        os.close(write_end)
    assert proc.stderr.decode() == ""
    assert proc.returncode == 1


def test_a_closed_stdout_at_start_still_runs_quietly():
    """`orthography2ipa --version >&-` starts with fd 1 closed, so sys.stdout is None."""
    proc = subprocess.run(
        [sys.executable, "-c",
         "import os, sys; os.close(1); sys.stdout = None; "
         "sys.argv = ['orthography2ipa', '--version']; "
         "from orthography2ipa.cli import main; main()"],
        stderr=subprocess.PIPE, timeout=120)
    assert proc.stderr.decode() == ""
    assert proc.returncode == 0


def test_an_error_after_the_reader_closed_still_reports():
    """A real error keeps its traceback when buffered output meets a closed pipe."""
    read_end, write_end = os.pipe()
    os.close(read_end)
    try:
        proc = subprocess.run(
            [sys.executable, "-c",
             "from orthography2ipa import cli\n"
             "def _run(argv):\n"
             "    print('partial output')\n"
             "    raise RuntimeError('boom')\n"
             "cli._run = _run\n"
             "cli.main([])\n"],
            stdout=write_end, stderr=subprocess.PIPE, timeout=120)
    finally:
        os.close(write_end)
    assert "RuntimeError: boom" in proc.stderr.decode()
    assert proc.returncode != 0
