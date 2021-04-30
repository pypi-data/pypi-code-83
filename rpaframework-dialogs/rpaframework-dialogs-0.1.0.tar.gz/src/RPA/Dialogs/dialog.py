import logging
import multiprocessing
import os
import sys
import time
from pathlib import Path
from queue import Empty
from typing import Dict, Union, Any, Optional

import webview  # type: ignore
from .types import Elements, Result
from .bridge import Bridge

LOGGER = logging.getLogger(__name__)


def static() -> str:
    # NB: pywebview uses sys.argv[0] as base
    base = Path(sys.argv[0]).resolve().parent
    path = Path(__file__).resolve().parent / "static"
    return os.path.relpath(str(path), str(base))


def run(
    queue: multiprocessing.Queue, elements: Elements, options: Dict[str, Any]
) -> None:
    """Start webview window with given options.
    Not part of Dialog class to prevent pickling of the entire instance.
    """
    debug = options.pop("debug", False)
    auto_height = options.pop("auto_height", False)

    bridge = Bridge(elements, auto_height)

    try:
        window = webview.create_window(js_api=bridge, **options)
        bridge.window = window

        LOGGER.debug("Starting dialog")
        webview.start(debug=debug)

        if bridge.error is not None:
            queue.put({"error": bridge.error})
        if bridge.result is not None:
            queue.put({"value": bridge.result})
        else:
            queue.put({"error": RuntimeError("Aborted by user")})
    except Exception as err:  # pylint: disable=broad-except
        queue.put({"error": err})
    finally:
        LOGGER.debug("Dialog closed")


class TimeoutException(RuntimeError):
    """Timeout while waiting for dialog to finish."""


class Dialog:
    """Container for a dialog running in a separate subprocess."""

    def __init__(
        self,
        elements: Elements,
        title: str,
        width: int,
        height: Union[int, str],
        on_top: bool,
        debug: bool = False,
    ):
        self.logger = logging.getLogger(__name__)
        self.timestamp = time.time()

        auto_height = height == "AUTO"
        if auto_height:
            height = 100

        self._elements = elements
        self._options = {
            "url": os.path.join(static(), "index.html"),
            "title": str(title),
            "width": int(width),
            "height": int(height),
            "auto_height": bool(auto_height),
            "on_top": bool(on_top),
            "debug": bool(debug),
            "text_select": True,
            "resizable": True,
            "background_color": "#0b1025",
        }

        self._result: Optional[Result] = None
        self._queue: multiprocessing.Queue = multiprocessing.Queue()
        self._process = multiprocessing.Process(
            target=run, args=(self._queue, self._elements, self._options)
        )

    @property
    def is_open(self) -> bool:
        return self._process.is_alive()

    def start(self) -> None:
        self._process.start()

    def stop(self, timeout: int = 15) -> None:
        if self._process.is_alive():
            self._process.terminate()

        try:
            self._result = self._queue.get(block=False)
        except Empty:
            pass

        self._process.join(timeout)
        if self._process.is_alive():
            self._process.kill()

        if not self._result:
            self._result = {"error": "Stopped by execution"}

    def poll(self) -> bool:
        if self._result is not None:
            return True

        try:
            self._result = self._queue.get(block=False)
            self._process.join(1)
            self.stop(5)
            return True
        except Empty:
            return False

    def wait(self, timeout: int = 180) -> None:
        if self._result is not None:
            return

        try:
            self._result = self._queue.get(block=True, timeout=timeout)
            self._process.join(1)
        except Empty as err:
            raise TimeoutException from err
        finally:
            self.stop(5)

    def result(self) -> Result:
        if self._result is None:
            raise RuntimeError("No result set, call poll() or wait() first")

        if "error" in self._result:
            raise self._result["error"]

        return self._result["value"]
