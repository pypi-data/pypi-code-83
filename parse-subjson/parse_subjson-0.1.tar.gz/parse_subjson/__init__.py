
dt = {}

def parse_json_recursively(json_object):
    """funcion recursiva que permite obtener el clave-valor
    mas anida en el subjson
    """
    if type(json_object) is dict and json_object:
        for key in json_object:
            if type(json_object[key]) is str and json_object:
                # print("{}: {}".format(key, json_object[key]))
                dt[key] = json_object[key]
            parse_json_recursively(json_object[key])

    elif type(json_object) is list and json_object:
        for item in json_object:
            parse_json_recursively(item)


def call_parser(d):
    parse_json_recursively(d)
    return dt
