"""Provides simple functions for parsing and modifying BOTW save data"""
import json
import os
import struct
from functools import lru_cache
from typing import ByteString, Dict, List, Union

VERSION = "0.1.0"
DataEntry = List[str]
Value = Union[bool, int, float, list, str]
SaveData = Dict[str, Value]
PathLike = Union[str, bytes, os.PathLike]


@lru_cache(1)
def _gamedata() -> Dict[str, DataEntry]:
    with open(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), "gamedata.json"),
        "r",
        encoding="utf-8",
    ) as file:
        return json.load(file)


class UnknownNodeTypeException(Exception):
    pass


def parse_file(file: PathLike) -> SaveData:
    """Parses a BOTW save file (.sav) and returns the contents as a dict.

    Args:
        file (PathLike): Path to the save file to parse

    Returns:
        SaveData: A dict of save flag data
    """   
    with open(file, "rb") as save_file:
        return parse(save_file.read())


def parse(file_data: ByteString) -> SaveData:
    """Parses a BOTW save data from bytes and returns the contents as a dict.

    Args:
        file_data (ByteString): Binary data of the save to parse

    Returns:
        SaveData: A dict of save flag data
    """   
    assert file_data[4:0xC] == b"\xff\xff\xff\xff\x00\x00\x00\x01"
    assert file_data[-4:] == b"\xff\xff\xff\xff"

    parsed_data: SaveData = {}
    gamedata: Dict[str, DataEntry] = _gamedata()

    i = 0xC
    while i < len(file_data) - 4:
        hashvalue: int
        hashvalue, entrydata = struct.unpack(">i4s", file_data[i : i + 8])
        if str(hashvalue) not in gamedata:
            i += 8
            continue
        datatype: str
        name: str
        datatype, name = gamedata[str(hashvalue)]
        if datatype == "s32":
            parsed_data[name] = struct.unpack(">i", entrydata)[0]
            i += 8
        elif datatype == "bool":
            parsed_data[name] = bool(struct.unpack(">i", entrydata)[0])
            i += 8
        elif datatype == "string256":
            bytestr = b""
            for j in range(i, i + 256 * 2, 8):
                bytestr += file_data[j + 4 : j + 8]
            parsed_data[name] = bytestr.split(b"\0", 1)[0].decode("ascii")
            i += 256 * 2
        elif datatype == "s32_array":
            if name not in parsed_data:
                parsed_data[name] = []
            parsed_data[name].append(struct.unpack(">i", entrydata)[0])
            i += 8
        elif datatype == "string64_array":
            if name not in parsed_data:
                parsed_data[name] = []
            bytestr = b""
            for j in range(i, i + 64 * 2, 8):
                bytestr += file_data[j + 4 : j + 8]
            parsed_data[name].append(bytestr.split(b"\0", 1)[0].decode("ascii"))
            i += 64 * 2
        elif datatype == "f32":
            parsed_data[name] = struct.unpack(">f", entrydata)[0]
            i += 8
        elif datatype == "string":
            bytestr = b""
            for j in range(i, i + 32 * 2, 8):
                bytestr += file_data[j + 4 : j + 8]
            parsed_data[name] = bytestr.split(b"\0", 1)[0].decode("ascii")
            i += 32 * 2
        elif datatype == "string64":
            bytestr = b""
            for j in range(i, i + 64 * 2, 8):
                bytestr += file_data[j + 4 : j + 8]
            parsed_data[name] = bytestr.split(b"\0", 1)[0].decode("ascii")
            i += 64 * 2
        elif datatype == "vector3f":
            parsed_data[name] = []
            for j in range(i, i + 3 * 8, 8):
                parsed_data[name].append(
                    struct.unpack(">f", file_data[j + 4 : j + 8])[0]
                )
            i += 3 * 8
        elif datatype == "string256_array":
            if name not in parsed_data:
                parsed_data[name] = []
            bytestr = b""
            for j in range(i, i + 256 * 2, 8):
                bytestr += file_data[j + 4 : j + 8]
            parsed_data[name].append(bytestr.split(b"\0", 1)[0].decode("ascii"))
            i += 256 * 2
        elif datatype == "bool_array":
            if name not in parsed_data:
                parsed_data[name] = []
            parsed_data[name].append(bool(struct.unpack(">i", entrydata)[0]))
            i += 8
        elif datatype == "vector2f_array":
            if name not in parsed_data:
                parsed_data[name] = []
            parsed_data[name].append([])
            for j in range(i, i + 2 * 8, 8):
                parsed_data[name][-1].append(
                    struct.unpack(">f", file_data[j + 4 : j + 8])[0]
                )
            i += 2 * 8
        elif datatype == "f32_array":
            if name not in parsed_data:
                parsed_data[name] = []
            parsed_data[name].append(struct.unpack(">f", entrydata)[0])
            i += 8
        elif datatype == "vector3f_array":
            if name not in parsed_data:
                parsed_data[name] = []
            parsed_data[name].append([])
            for j in range(i, i + 3 * 8, 8):
                parsed_data[name][-1].append(
                    struct.unpack(">f", file_data[j + 4 : j + 8])[0]
                )
            i += 3 * 8
        else:
            raise UnknownNodeTypeException(datatype)
    return parsed_data


def update_file(file: PathLike, save_data: SaveData):
    """Updates a BOTW save file with modified save data content from a dict.

    Args:
        file (PathLike): Path of the save file to update
        save_data (SaveData): Dict of save data to update with
    """    
    with open(file, "rb") as save_file:
        update(save_file.read(), save_data)


def update(file_data: ByteString, save_data: SaveData) -> bytes:
    """Updates binary BOTW save data with modified save data content from a dict.

    Args:
        file_data (ByteString): Binary data of the save to update
        save_data (SaveData): Dict of save data to update with
    """    
    assert file_data[4:0xC] == list(b"\xff\xff\xff\xff\x00\x00\x00\x01")
    assert file_data[-4:] == list(b"\xff\xff\xff\xff")

    gamedata: Dict[str, DataEntry] = _gamedata()

    i = 0xC
    while i < len(file_data) - 4:
        hashvalue: int = struct.unpack(">i", bytes(file_data[i : i + 4]))[0]
        if str(hashvalue) not in gamedata:
            i += 8
            continue
        datatype: str
        name: str
        datatype, name = gamedata[str(hashvalue)]
        value = save_data[name]
        if datatype == "s32":
            file_data[i + 4 : i + 8] = struct.pack(">i", value)
            i += 8
        elif datatype == "bool":
            file_data[i + 4 : i + 8] = struct.pack(">i", value)
            i += 8
        elif datatype == "string256":
            value += "\0" * (256 - len(value))
            for j in range(256 // 4):
                file_data[i + 4 + j * 8 : i + 8 + j * 8] = value[
                    j * 4 : j * 4 + 4
                ].encode("ascii")
            i += 256 * 2
        elif datatype == "s32_array":
            file_data[i + 4 : i + 8] = struct.pack(">i", value[0])
            save_data[name] = save_data[name][1:]
            i += 8
        elif datatype == "string64_array":
            value[0] += "\0" * (64 - len(value[0]))
            for j in range(64 // 4):
                file_data[i + 4 + j * 8 : i + 8 + j * 8] = value[0][
                    j * 4 : j * 4 + 4
                ].encode("ascii")
            save_data[name] = save_data[name][1:]
            i += 64 * 2
        elif datatype == "f32":
            file_data[i + 4 : i + 8] = struct.pack(">f", value)
            i += 8
        elif datatype == "string":
            value += "\0" * (32 - len(value))
            for j in range(32 // 4):
                file_data[i + 4 + j * 8 : i + 8 + j * 8] = value[
                    j * 4 : j * 4 + 4
                ].encode("ascii")
            i += 32 * 2
        elif datatype == "string64":
            value += "\0" * (64 - len(value))
            for j in range(64 // 4):
                file_data[i + 4 + j * 8 : i + 8 + j * 8] = value[
                    j * 4 : j * 4 + 4
                ].encode("ascii")
            i += 64 * 2
        elif datatype == "vector3f":
            for j in range(3):
                file_data[i + 4 + j * 8 : i + 8 + j * 8] = struct.pack(">f", value[j])
            i += 3 * 8
        elif datatype == "string256_array":
            value[0] += "\0" * (256 - len(value[0]))
            for j in range(256 // 4):
                file_data[i + 4 + j * 8 : i + 8 + j * 8] = value[0][
                    j * 4 : j * 4 + 4
                ].encode("ascii")
            save_data[name] = save_data[name][1:]
            i += 256 * 2
        elif datatype == "bool_array":
            file_data[i + 4 : i + 8] = struct.pack(">i", value[0])
            save_data[name] = save_data[name][1:]
            i += 8
        elif datatype == "vector2f_array":
            for j in range(2):
                file_data[i + 4 + j * 8 : i + 8 + j * 8] = struct.pack(
                    ">f", value[0][j]
                )
            save_data[name] = save_data[name][1:]
            i += 2 * 8
        elif datatype == "f32_array":
            file_data[i + 4 : i + 8] = struct.pack(">f", value[0])
            save_data[name] = save_data[name][1:]
            i += 8
        elif datatype == "vector3f_array":
            for j in range(3):
                file_data[i + 4 + j * 8 : i + 8 + j * 8] = struct.pack(
                    ">f", value[0][j]
                )
            save_data[name] = save_data[name][1:]
            i += 3 * 8
        else:
            raise UnknownNodeTypeException(datatype)
    return bytes(file_data)
