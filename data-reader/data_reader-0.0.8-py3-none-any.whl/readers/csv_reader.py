import os


class CSVReader:

    def __init__(self, file_path, arguments={'separator': ','}):
        self.__file_path = file_path
        self.__arguments = arguments

        self.__initialize()

    def __initialize(self):
        """ Prepares and validates argument. """

        if 'separator' not in self.__arguments:
            raise Exception('"separator" argument is required to parse CSV.')

        self.__separator = self.__arguments['separator']
        self.__skip_header = True
        self.__enclosing = '"'

        if 'skip_header' in self.__arguments:
            self.__skip_header = self.__arguments['skip_header']
        if 'enclosing' in self.__arguments:
            self.__enclosing = self.__arguments['enclosing']

    def iterate(self):
        """ allows iteration over parsed data objects with a python generator. """

        with open(self.__file_path) as f:
            for index, line in enumerate(f):
                if index == 0 and self.__skip_header:
                    continue

                obj = self.__parseLine(line)
                yield obj

    def __parseLine(self, line):
        """ Parses a line into python dictionary object """

        split = line.split(self.__separator)
        formatted = []

        if self.__enclosing is not None:
            for entry in split:
                if entry.startswith(self.__enclosing) and entry.endswith(self.__enclosing):
                    entry = entry[1:]
                    entry = entry[:-1]
                    formatted.append(entry)
                else:
                    formatted.append(entry)

        del split

        return formatted
