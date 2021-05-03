import os
import time
import zlib
import datetime
import argparse
import logging

import psutil
import plotext as plt
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

__version__ = '0.1.1'
__author__ = 'The memory-monitor-cli Authors'

logger = logging.getLogger(__name__)


def take_snapshot():
    logger.debug('inside take_snapshot()')
    timestamp = int(datetime.datetime.now().timestamp())
    snapshot = psutil.virtual_memory()
    used_memory_percentage = round(snapshot.used / snapshot.total * 100, 2)
    return timestamp, used_memory_percentage


def save(snapshots, output_filename):
    logger.debug('inside stream_to()')
    lines = []
    for snapshot in snapshots:
        timestamp = snapshot[0]
        percentage = snapshot[1]
        lines.append(f'{timestamp} {percentage}')
    data = os.linesep.join(lines)
    compressed_data = zlib.compress(data.encode())

    with open(output_filename, 'wb') as f:
        f.write(compressed_data)


def show(snapshots):
    logger.debug('inside show()')
    timestamps = [s[0] for s in snapshots]
    percentages = [s[1] for s in snapshots]

    xticks = timestamps
    xlabels = [datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')
               for timestamp in timestamps]

    yticks = list(range(0, 101, 10))
    ylabels = [f'{percentage} %' for percentage in yticks]

    plt.clp()
    plt.clt()
    plt.plot(timestamps, percentages)
    plt.ylim(0, 100)
    plt.xticks(xticks, xlabels)
    plt.yticks(yticks, ylabels)
    plt.nocolor()
    plt.show()


def monitor_memory(time_window, time_unit, frequency, output_filename=None):
    logger.debug('inside monitor_memory()')
    in_seconds = {
        's': 1,
        'm': 1 * 60,
        'h': 1 * 60 * 60,
        'd': 1 * 60 * 60 * 24,
    }
    snapshots = []
    max_len = int(frequency * time_window)

    while True:
        snapshot = take_snapshot()
        snapshots.append(snapshot)

        if len(snapshots) > max_len:
            del snapshots[0]

        if output_filename is not None:
            save(snapshots, output_filename)
        else:
            show(snapshots)
        time.sleep(in_seconds[time_unit] / frequency)


def command_run(argv):
    logger.debug('inside command_run()')
    assert argv.time_window > 0
    assert argv.frequency > 0
    monitor_memory(argv.time_window, argv.time_unit, argv.frequency, argv.stream_to_file)


class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        logger.debug('inside FileEventHandler.on_created()')
        super().on_created(event)
        self._show(event.src_path)

    def on_modified(self, event):
        logger.debug('inside FileEventHandler.on_modified()')
        super().on_modified(event)
        self._show(event.src_path)

    def _show(self, stream_from_file):
        logger.debug('inside FileEventHandler._show()')
        if not stream_from_file:
            return

        with open(stream_from_file, 'rb') as f:
            compressed_data = f.read()

        try:
            data = zlib.decompress(compressed_data).decode()
        except zlib.error as e:
            return

        snapshots = list(map(
            lambda snapshot: (int(snapshot[0]), round(float(snapshot[1]), 2)),
            map(lambda line: line.split(), data.splitlines())))

        show(snapshots)


def command_show(argv):
    logger.debug('inside command_show()')
    event_handler = FileEventHandler()
    observer = Observer()
    observer.schedule(event_handler, argv.stream_from_file)
    observer.start()

    try:
        while True:
            time.sleep(10)
    finally:
        observer.stop()
        observer.join()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--logging-level', choices=('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'), default='INFO')

    subparsers = parser.add_subparsers()

    parser_run = subparsers.add_parser('run')
    parser_run.add_argument('--time-window', type=float, default=1)
    parser_run.add_argument('--time-unit', choices='smhd', default='m')
    parser_run.add_argument('--frequency', type=int, default=60)
    parser_run.add_argument('--stream-to-file')
    parser_run.set_defaults(delegate=command_run)

    parser_show = subparsers.add_parser('show')
    parser_show.add_argument('--stream-from-file', required=True)
    parser_show.set_defaults(delegate=command_show)

    # argv = parser.parse_args(
    #    '--logging-level=DEBUG run --time-window=1 --time-unit=m --frequency=20 --stream-to-file=memory-usage.gz'.split()
    # )
    # argv = parser.parse_args(
    #    'show --stream-from-file=memory-usage.gz'.split()
    # )

    argv = parser.parse_args()

    logging.basicConfig()
    logger.setLevel(argv.logging_level)

    argv.delegate(argv)
