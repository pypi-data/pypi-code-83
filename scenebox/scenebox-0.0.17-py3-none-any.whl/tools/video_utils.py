"""Miscellaneous (catch all) tools Copyright 2020 Caliber Data Labs."""

#  Copyright (c) 2020 Caliber Data Labs.
#  All rights reserved.
#
from typing import NamedTuple

import ffmpeg


class VideoProperties(NamedTuple):
    width: int
    height: int
    fps: float
    duration: float
    num_frames: int


def get_video_attributes(video_uri: str) -> NamedTuple:
    info = ffmpeg.probe(video_uri)
    return VideoProperties(
        width = info['streams'][0]['width'],
        height = info['streams'][0]['height'],
        duration = info['streams'][0]['duration'],
        num_frames = info['streams'][0]['nb_frames'],
        fps = info['streams'][0]['avg_frame_rate'],
    )


