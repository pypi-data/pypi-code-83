# -*- coding: utf-8 -*-

"""Main module."""
from __future__ import absolute_import, print_function

import difflib
import json
import os
import sys
import threading
import time
import unittest

pygmentspresent = False
# ANSI color is unsupported prior to Windows 10
if os.name != "nt":
    try:  # is pygments installed
        import pygments
        import pygments.formatters as formatters
        import pygments.lexer as lexer
        import pygments.lexers as lexers
        import pygments.style as style
        import pygments.token as token

        pygmentspresent = True
        difflexer = lexers.DiffLexer()
        terminal256formatter = formatters.Terminal256Formatter()
    except ImportError:
        pass

if pygmentspresent:

    class TestRunnerStyle(style.Style):
        default_style = ""
        skipped = token.string_to_tokentype("Token.Generic.Skipped")
        failed = token.string_to_tokentype("Token.Generic.Failed")
        skippedname = token.string_to_tokentype("Token.Generic.SName")
        failedname = token.string_to_tokentype("Token.Generic.FName")
        styles = {
            skipped: "#e5e5e5",
            skippedname: "#00ffff",
            failed: "#7f0000",
            failedname: "#ff0000",
        }

    class TestRunnerLexer(lexer.RegexLexer):
        testpattern = r"[\w-]+\.(t|py)(#[^\s]+)?"
        tokens = {
            "root": [
                (r"^Skipped", token.Generic.Skipped, "skipped"),
                (r"^Failed ", token.Generic.Failed, "failed"),
                (r"^ERROR: ", token.Generic.Failed, "failed"),
            ],
            "skipped": [
                (testpattern, token.Generic.SName),
                (r":.*", token.Generic.Skipped),
            ],
            "failed": [
                (testpattern, token.Generic.FName),
                (r"(:| ).*", token.Generic.Failed),
            ],
        }

    runnerformatter = formatters.Terminal256Formatter(style=TestRunnerStyle)
    runnerlexer = TestRunnerLexer()

if sys.version_info > (3, 5, 0):
    PYTHON3 = True

    def _bytespath(p):
        if p is None:
            return p
        return p.encode("utf-8")

    def _strpath(p):
        if p is None:
            return p
        return p.decode("utf-8")


elif sys.version_info >= (3, 0, 0):
    print(
        "%s is only supported on Python 3.5+ and 2.7, not %s"
        % (sys.argv[0], ".".join(str(v) for v in sys.version_info[:3]))
    )
    sys.exit(70)  # EX_SOFTWARE from `man 3 sysexit`
else:
    PYTHON3 = False

    # In python 2.x, path operations are generally done using
    # bytestrings by default, so we don't have to do any extra
    # fiddling there. We define the wrapper functions anyway just to
    # help keep code consistent between platforms.
    def _bytespath(p):
        return p

    _strpath = _bytespath

PYTHON = _bytespath(sys.executable.replace("\\", "/"))


_unified_diff = difflib.unified_diff
if PYTHON3:
    import functools

    _unified_diff = functools.partial(difflib.diff_bytes, difflib.unified_diff)


def getdiff(expected, output, ref, err):
    servefail = False
    lines = []
    for line in _unified_diff(expected, output, ref, err):
        if line.startswith(b"+++") or line.startswith(b"---"):
            line = line.replace(b"\\", b"/")
            if line.endswith(b" \n"):
                line = line[:-2] + b"\n"
        lines.append(line)
        if not servefail and line.startswith(
            b"+  abort: child process failed to start"
        ):
            servefail = True

    return servefail, lines


verbose = False


def log(*msg):
    """Log something to stdout.

    Arguments are strings to print.
    """
    with iolock:
        if verbose:
            print(verbose, end=" ")
        for m in msg:
            print(m, end=" ")
        print()
        sys.stdout.flush()


def highlightmsg(msg, color):
    if not color:
        return msg
    assert pygmentspresent
    return pygments.highlight(msg, runnerlexer, runnerformatter)


iolock = threading.RLock()
firsterror = False

def to_unicode_scalar(scalar):
    try:
        return scalar.decode("utf-8")
    except Exception:
        return scalar

def to_unicode_list(_list):
    return [to_unicode_scalar(x) for x in _list]

class TestResult(unittest._TextTestResult):
    """Holds results when executing via unittest."""

    # Don't worry too much about accessing the non-public _TextTestResult.
    # It is relatively common in Python testing tools.
    def __init__(self, options, *args, **kwargs):
        super(TestResult, self).__init__(*args, **kwargs)
        self.start = time.time()
        print("START?", self.start)

        self._options = options

        # unittest.TestResult didn't have skipped until 2.7. We need to
        # polyfill it.
        self.skipped = []

        # We have a custom "ignored" result that isn't present in any Python
        # unittest implementation. It is very similar to skipped. It may make
        # sense to map it into skip some day.
        self.ignored = []

        self.times = []
        self._firststarttime = None
        # Data stored for the benefit of generating xunit reports.
        self.successes = []
        self.faildata = {}

        self.stop = None

        if options.color == "auto":
            self.color = pygmentspresent and self.stream.isatty()
        elif options.color == "never":
            self.color = False
        else:  # 'always', for testing purposes
            self.color = pygmentspresent

    def onStart(self, tests):
        if hasattr(tests, "_tests"):
            test_number = len(tests._tests)
        else:
            test_number = len(tests)
        with iolock:
            print(json.dumps({"_type": "session_start", "test_number": test_number}))

    def onEnd(self):
        self.stop = time.time()
        data = {
            "skipped": 0,
            "failed": 0,
            "error": 0,
            "total_duration": self.stop - self.start,
            "passed": 0,
            "_type": "session_end",
        }

        with iolock:
            print(json.dumps(data))

    def addFailure(self, test, reason):
        self.failures.append((test, reason))
        if reason == "output changed":
            # Ignore output changed as we should already displayed it
            return

        if self._options.first:
            self.stop()
        else:
            with iolock:
                if reason == "timed out":
                    self.stream.write("t")
                else:
                    if not self._options.nodiff:
                        self.stream.write("\n")
                        # Exclude the '\n' from highlighting to lex correctly
                        formatted = "ERROR: %s output changed\n" % test
                        self.stream.write(highlightmsg(formatted, self.color))
                    self.stream.write("!")

                self.stream.flush()

    def addSuccess(self, test):
        if test._finished is None:
            return self._add_collection(test)

        # print("ADD SUCCESS", test, repr(test), test.__dict__)

        starttime = test.started
        # endtime = test.stopped
        endtime = os.times()
        real_time = endtime[4] - starttime[4]

        test_file = to_unicode_scalar(test.bname)

        data = {
            "stderr": "",
            "_type": "test_result",
            "skipped_messages": {},
            "outcome": "passed",
            "durations": {},
            "duration": real_time,
            "line": 1,
            "file": test_file,
            "error": {"humanrepr": ""},
            "test_name": test.name,
            "stdout": "",
            "id": test.name,
        }

        with iolock:
            print(json.dumps(data))

        self.successes.append(test)

    def _add_collection(self, test):
        test_file = to_unicode_scalar(test.bname)

        data = {
            "_type": "test_collection",
            "test_name": test.name,
            "id": test.name,
            "file": test_file,
            "line": 1,
        }

        with iolock:
            print(json.dumps(data))

    def addError(self, test, err):
        starttime = test.started
        # endtime = test.stopped
        endtime = os.times()
        real_time = endtime[4] - starttime[4]

        import traceback
        traceback.print_exception(*err)

        test_file = to_unicode_scalar(test.bname)

        data = {
            "stderr": "",
            "_type": "test_result",
            "skipped_messages": {},
            "outcome": "failed",
            "durations": {},
            "duration": real_time,
            "line": 1,
            "file": test_file,
            "error": {"humanrepr": str(err)},
            "test_name": test.name,
            "stdout": "",
            "id": test.name,
        }

        print(json.dumps(data))
        # super(TestResult, self).addError(test, err)
        if self._options.first:
            self.stop()

    # Polyfill.
    def addSkip(self, test, reason):
        starttime = test.started
        # endtime = test.stopped
        endtime = os.times()
        real_time = endtime[4] - starttime[4]

        test_file = to_unicode_scalar(test.bname)

        data = {
            "stderr": "",
            "_type": "test_result",
            "skipped_messages": {"test": reason},
            "outcome": "skipped",
            "durations": {},
            "duration": real_time,
            "line": 1,
            "file": test_file,
            "error": {"humanrepr": ""},
            "test_name": test.name,
            "stdout": "",
            "id": test.name,
        }
        print(json.dumps(data))
        self.skipped.append((test, reason))

    def addIgnore(self, test, reason):
        self.ignored.append((test, reason))
        with iolock:
            if self.showAll:
                self.stream.writeln("ignored %s" % reason)
            else:
                if reason not in ("not retesting", "doesn't match keyword"):
                    self.stream.write("i")
                else:
                    self.testsRun += 1
                self.stream.flush()

    def addOutputMismatch(self, test, ret, got, expected):
        """Record a mismatch in test output for a particular test."""
        if self.shouldStop or firsterror:
            # don't print, some other test case already failed and
            # printed, we're just stale and probably failed due to our
            # temp dir getting cleaned up.
            return

        starttime = test.started
        # endtime = test.stopped
        endtime = os.times()
        real_time = endtime[4] - starttime[4]

        test_file = to_unicode_scalar(test.bname)

        _, lines = getdiff(expected, got, test.refpath, test.errpath)

        data = {
            "stderr": "",
            "_type": "test_result",
            "skipped_messages": {},
            "outcome": "failed",
            "durations": {},
            "duration": real_time,
            "line": 1,
            "file": test_file,
            "error": {"diff": {"got": to_unicode_list(got), "expected": to_unicode_list(expected), "diff": to_unicode_list(lines)}},
            "test_name": test.name,
            "stdout": "",
            "id": test.name,
        }
        print(json.dumps(data))

    def startTest(self, test):
        super(TestResult, self).startTest(test)

        # os.times module computes the user time and system time spent by
        # child's processes along with real elapsed time taken by a process.
        # This module has one limitation. It can only work for Linux user
        # and not for Windows.
        test.started = os.times()
        if self._firststarttime is None:  # thread racy but irrelevant
            self._firststarttime = test.started[4]

    def stopTest(self, test, interrupted=False):
        super(TestResult, self).stopTest(test)

        test.stopped = os.times()

        starttime = test.started
        endtime = test.stopped
        origin = self._firststarttime
        self.times.append(
            (
                test.name,
                endtime[2] - starttime[2],  # user space CPU time
                endtime[3] - starttime[3],  # sys  space CPU time
                endtime[4] - starttime[4],  # real time
                starttime[4] - origin,  # start date in run context
                endtime[4] - origin,  # end date in run context
            )
        )

        if interrupted:
            with iolock:
                self.stream.writeln(
                    "INTERRUPTED: %s (after %d seconds)"
                    % (test.name, self.times[-1][3])
                )
