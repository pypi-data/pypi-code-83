import ijson
import os


class JSONReader:

    def __init__(self, file_path, arguments={}):
        self.__file_path = file_path
        self.__arguments = arguments

        self.__item_node = 'item'
        if 'node_path' in arguments:
            self.__item_node = arguments['node_path']

    def iterate(self):
        """ Iterates over JSON file stream. """

        with open(self.__file_path, 'rb') as fh:
            parsed_json = ijson.items(fh, self.__item_node)

            for object in parsed_json:
                yield object
