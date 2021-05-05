#!/usr/bin/env python3


"""
La classe IDGenerator è stata pensate per facilitare la creazione di ID da associare ad altri oggetti
"""


__author__ = "Stefano Gigli"
__copyright__ = "Copyright 2019, SG Software"
__credits__ = []
__license__ = "GPL"
__version__ = "0.9"
__maintainer__ = "Stefano Gigli"
__email__ = "exe.dev.exe@gmail.com"
__status__ = "Beta version"


from random import choice


class IDGenerator:
    ID_GENERATOR_DEFAULT_LEN = 8
    ID_GENERATOR_DEFAULT_SEED_STR = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"

    def __init__(self, i_idg_len=ID_GENERATOR_DEFAULT_LEN, s_idg_seed_str=ID_GENERATOR_DEFAULT_SEED_STR):
        self.i_idg_len = i_idg_len
        self.s_idg_seed_str = s_idg_seed_str

    def generate_id(self) -> str:
        s_new_id = ""
        for index in range(0, self.i_idg_len):
            s_new_id += choice(self.s_idg_seed_str)
        return s_new_id

    def generate_customized_id(self, s_item_class_name: str = "Unknown_Class", s_item_title: str = "Unknown_Title") -> str:
        return "___ID___" + s_item_class_name + "___" + s_item_title.replace(" ", "_") + "___" + self.generate_id() + "___"


if __name__ == '__main__':
    generator = IDGenerator()
    print(generator.generate_customized_id())
