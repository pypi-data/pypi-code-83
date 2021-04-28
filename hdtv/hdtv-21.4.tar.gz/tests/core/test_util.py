# -*- coding: utf-8 -*-

# HDTV - A ROOT-based spectrum analysis software
#  Copyright (C) 2006-2009  The HDTV development team (see file AUTHORS)
#
# This file is part of HDTV.
#
# HDTV is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 2 of the License, or (at your
# option) any later version.
#
# HDTV is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
# for more details.
#
# You should have received a copy of the GNU General Public License
# along with HDTV; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA

import pytest

import hdtv.util


@pytest.mark.parametrize(
    "cmdline, segs, last_suffix",
    [
        ("", [], ""),
        ("a", [["a"]], ""),
        ("a;", [["a"]], ""),
        ("a;b", [["a"], ["b"]], ""),
        ("a ;b", [["a"], ["b"]], ""),
        ("a; b", [["a"], ["b"]], ""),
        ("a ; b", [["a"], ["b"]], ""),
        (" a ; b", [["a"], ["b"]], ""),
        ("a;b c", [["a"], ["b", "c"]], ""),
        ('a;b "c d"', [["a"], ["b", "c d"]], ""),
        ('a "b', [["a", "b"]], '"'),
        ('a ";', [["a", ";"]], '"'),
        ("a#b", [["a"]], ""),
        ('a "" a', [["a", "", "a"]], ""),
    ],
)
def test_SplitCmdlines(cmdline, segs, last_suffix):
    res_segs, res_last_suffix = hdtv.util.SplitCmdlines(cmdline)
    assert segs == res_segs
    assert last_suffix == res_last_suffix
