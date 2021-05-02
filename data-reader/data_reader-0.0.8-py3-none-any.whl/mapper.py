from data_reader.utils import Accessor, Logger
import types
import os


class Mapper:

    def __init__(self, mapping):
        self.__mapping = mapping
        self.__input = None

    def transform(self, data):
        self.__input = data
        result = {}
        for (key, map_value) in self.__mapping.items():
            path = map_value['path']
            value = Accessor.get(self.__input, path)

            instance_data = self.__input
            processed_value = value

            # if self.__ondata is not None and type(self.__ondata) is str:
            #     try:
            #         exec(self.__ondata)
            #     except Exception as e:
            #         Logger.warning(f'could not execute "ondata" callback. reason: {e}')


            result = Accessor.set(result, key, value)

        # if self.__onfinish is not None and type(self.__onfinish) is str:
        #     try:
        #         exec(self.__onfinish)
        #     except Exception as e:
        #         Logger.warning(f'could not execute "onfinish" callback. reason: {e}')

        return result
