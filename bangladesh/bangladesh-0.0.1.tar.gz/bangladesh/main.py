import json


def get_divisions():
    # with json load  (file)
    info = open('./json/divisions.json', encoding="utf8")
    json = json.load(info)
    return json


def get_districts():
    # with json load  (file)
    info = open('./json/districts.json', encoding="utf8")
    json = json.load(info)
    return json


def get_postcodes():
    # with json load  (file)
    info = open('./json/postcodes.json', encoding="utf8")
    json = json.load(info)
    return json


def get_upazilas():
    # with json load  (file)
    info = open('./json/upazilas.json', encoding="utf8")
    json = json.load(info)
    return json
