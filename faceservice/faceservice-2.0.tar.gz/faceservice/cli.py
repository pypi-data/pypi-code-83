"""Console script for faceservice."""
import sys
import click

import click

from faceservice.action import Action


@click.command()
@click.option('--video_path', default=r'./figure/test3.mp4', help='input the video path')
def main(video_path):
    action = Action()
    action.isNodeHead(video_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
