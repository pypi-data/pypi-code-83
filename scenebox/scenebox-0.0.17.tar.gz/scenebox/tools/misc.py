"""Miscellaneous (catch all) tools Copyright 2020 Caliber Data Labs."""

#  Copyright (c) 2020 Caliber Data Labs.
#  All rights reserved.
#
import hashlib
import json
import sys
import uuid
from typing import Dict


def decorate_all_inherited_methods(decorator):
    """Add a decorator to all methods which are not private.

    Usage:
        @decorate_all_inherited_methods(decorator)
        class C(object):
            def m1(self): pass
            def m2(self, x): pass
    ...
    """

    def decorate(cls):
        for attr in dir(cls):
            # Only callable methods and those that don't start with _ are
            # eligible
            if callable(getattr(cls, attr)) and not attr.startswith("_"):
                # Only inherited or overrided methods are eligible
                if attr not in cls.__dict__ or hasattr(super(cls), attr):
                    setattr(cls, attr, decorator(getattr(cls, attr)))
        return cls

    return decorate


def chunk_list(list_elements, chunk_size):
    """Chunks a list into chunk_size chunks, with last chunk the remaining
    elements.

    :param list_elements:
    :param chunk_size:
    :return:
    """
    chunks = []
    while True:
        if len(list_elements) > chunk_size:
            chunk = list_elements[0:chunk_size]
            list_elements = list_elements[chunk_size:]
            chunks.append(chunk)
        else:
            chunks.append(list_elements)
            break
    return chunks


def as_bool(s):
    if s is None:
        return False

    if isinstance(s, bool):
        return s
    else:
        s = str(s)  # In Python 2, handle case when s is unicode
        if s.lower() in {"t", "true"}:
            return True
        elif s.lower() in {"f", "false"}:
            return False
        else:
            raise ValueError(
                "Input of type ::: {} cannot be converted to bool ::: {}".format(
                    type(s), s))


def get_truncated_uid(n: int = 5):
    return get_guid()[0:n]


def get_guid():
    return str(uuid.uuid4()).replace('-', '_')


def get_md5_from_file(filename):
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def get_md5_from_string(string):
    m = hashlib.md5()
    m.update(string.encode("utf-8"))
    return m.hexdigest()


def hash_string_into_positive_integer(string) -> int:
    """return a signed 64-bit."""
    return abs((hash(string) + 2**63) % 2**64 - 2**63)



def get_md5_from_json_object(json_object: Dict):
    """get the md5 from a json object (dic, list, etc). We take care of sorting
    the keys here for repeatability.

    :param json_object: list, dic, etc
    :return: md5 of the object
    """
    return get_md5_from_string(json.dumps(json_object, sort_keys=True))


def parse_file_path(input_str: str) \
        -> (str, str, str, str):
    cleaned_str = input_str.replace("\\", "/")
    filename = cleaned_str.split("/")[-1]
    extension = filename.split(".")[-1]
    filename_no_extension = filename.replace("." + extension, "")
    path = cleaned_str.replace(filename, "")
    return filename, path, filename_no_extension, extension


def get_video_attributes(video_uri: str) -> NamedTuple:
    info = ffmpeg.probe(video_uri)
    return VideoProperties(
        width = info['streams'][0]['width'],
        height = info['streams'][0]['height'],
        duration = info['streams'][0]['duration'],
        num_frames = info['streams'][0]['nb_frames'],
        fps = info['streams'][0]['avg_frame_rate'],
    )