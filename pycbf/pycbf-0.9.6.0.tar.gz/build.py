import re
from distutils.core import Extension
from pathlib import Path, PurePath
from typing import Any, Dict

# import skbuild
# import skbuild.constants

CBF_SOURCES = [
    "cbflib/src/cbf.c",
    "cbflib/src/cbf_airy_disk.c",
    "cbflib/src/cbf_alloc.c",
    "cbflib/src/cbf_ascii.c",
    "cbflib/src/cbf_binary.c",
    "cbflib/src/cbf_byte_offset.c",
    "cbflib/src/cbf_canonical.c",
    "cbflib/src/cbf_codes.c",
    "cbflib/src/cbf_compress.c",
    "cbflib/src/cbf_context.c",
    "cbflib/src/cbf_copy.c",
    "cbflib/src/cbf_file.c",
    "cbflib/src/cbf_getopt.c",
    "cbflib/src/cbf_lex.c",
    "cbflib/src/cbf_minicbf_header.c",
    "cbflib/src/cbf_nibble_offset.c",
    "cbflib/src/cbf_packed.c",
    "cbflib/src/cbf_predictor.c",
    "cbflib/src/cbf_read_binary.c",
    "cbflib/src/cbf_read_mime.c",
    "cbflib/src/cbf_simple.c",
    "cbflib/src/cbf_string.c",
    "cbflib/src/cbf_stx.c",
    "cbflib/src/cbf_tree.c",
    "cbflib/src/cbf_ulp.c",
    "cbflib/src/cbf_uncompressed.c",
    "cbflib/src/cbf_write.c",
    "cbflib/src/cbf_write_binary.c",
    "cbflib/src/cbf_ws.c",
    "cbflib/src/cbff.c",
    "cbflib/src/fgetln.c",
    "cbflib/src/img.c",
    "cbflib/src/md5c.c",
    # "cbflib/src/cbf_hdf5.c",
    # "cbflib/src/cbf_hdf5_filter.c",
]
extensions = [
    Extension(
        "pycbf._pycbf",
        sources=["pycbf_wrap.c", *CBF_SOURCES],
        include_dirs=[str(PurePath(__file__).parent / "cbflib" / "include")],
        define_macros=[
            ("CBF_NO_REGEX", None),
            ("SWIG_PYTHON_STRICT_BYTE_CHAR", None),
        ],
    )
]


def build(setup_kwargs: Dict[str, Any]) -> None:
    # print("Build C Extensions Here")
    # Rewrite the cbf.h file to not require hdf5

    # Rewrite cbf.h so that it doesn't require HDF5.h (it doesn't need it)
    cbf_h = Path(__file__).parent.joinpath("cbflib", "include", "cbf.h")
    cbf_h_data = cbf_h.read_bytes()
    cbf_h_data_rw = re.sub(
        b'^#include "hdf5.h"', b'// #include "hdf5.h"', cbf_h_data, flags=re.MULTILINE
    )
    if cbf_h_data != cbf_h_data_rw:
        cbf_h.write_bytes(cbf_h_data_rw)

    setup_kwargs.update({"ext_modules": extensions})


if __name__ == "__main__":
    build()
