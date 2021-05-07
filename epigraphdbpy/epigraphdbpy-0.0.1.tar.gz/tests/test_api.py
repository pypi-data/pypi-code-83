#!/usr/local/bin/python3
import epigraphdbpy


def test_api():
    assert epigraphdbpy.ping_api() == True
