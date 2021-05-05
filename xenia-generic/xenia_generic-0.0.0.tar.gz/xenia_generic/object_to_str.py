#!/usr/bin/env python3


from inspect import stack  # usata solo nella funzione get_obj_name

from col_tex import ColTex  # usata per i codici dei colori


__author__ = "Stefano Gigli"
__copyright__ = "Copyright 2019, SG Software"
__credits__ = []
__license__ = "GPL"
__version__ = "0.9"
__maintainer__ = "Stefano Gigli"
__email__ = "exe.dev.exe@gmail.com"
__status__ = "Beta version"


# Costanti lettera per i vari TAGs
OTS_BEGIN_OBJ_TAG = " BEGIN"
OTS_END_OBJ_TAG = " END"
OTS_CLASS_TAG = " <class {}>"

# Colore usato per i TAGs
OTS_TAGS_COL = ColTex.ForegroundColor.CYAN

# Colore per None
OTS_NONE_COL = ColTex.Modifiers.BOLD + ColTex.ForegroundColor.RED

# Colori usati per i tipi di dato base
OTS_BASIC_TYPE_NAME_COL = ColTex.ForegroundColor.PURPLE
OTS_BASIC_TYPE_ATTR_COL = ColTex.ForegroundColor.WHITE
OTS_BASIC_TYPE_VALUE_COL = ColTex.ForegroundColor.WHITE
OTS_BASIC_TYPE_TOKEN_COL = ColTex.ForegroundColor.CYAN

# Colori usati per le liste
OTS_LIST_OBJ_COL = ColTex.ForegroundColor.YELLOW
OTS_LIST_CLASS_COL = ColTex.ForegroundColor.YELLOW

# Colori usati per le tuple
OTS_TUPLE_OBJ_COL = ColTex.ForegroundColor.BLUE
OTS_TUPLE_CLASS_COL = ColTex.ForegroundColor.BLUE

# Colori usati per i dizionari
OTS_DICT_OBJ_COL = ColTex.ForegroundColor.PINK
OTS_DICT_CLASS_COL = ColTex.ForegroundColor.PINK

# Colori usati per gli insiemi
OTS_SET_OBJ_COL = ColTex.ForegroundColor.LIGHT_RED
OTS_SET_CLASS_COL = ColTex.ForegroundColor.LIGHT_RED

# Colori usati per tutti gli altri oggetti
OTS_GENERIC_OBJ_COL = ColTex.ForegroundColor.WHITE
OTS_GENERIC_CLASS_COL = ColTex.ForegroundColor.RED + ColTex.Modifiers.BOLD


class ObjectToStr:
    @staticmethod
    def get_obj_name(obj: object) -> str:
        """
        Dato un oggetto restituisce il nome della variabile relativa a quell'oggetto
        :param obj: oggetto del quale recuperare il nome
        :return: una stringa che corrisponde al nome dell'oggetto obj
        """
        for fi in reversed(stack()):
            names = [var_name for var_name, var_val in fi.frame.f_locals.items() if var_val is obj]
            if len(names) > 0:
                return names[0]

    @staticmethod
    def remove_class_name(verbose_param_name: str) -> str:
        """
        Dato il nome di un attributo... se si tratta di un attributo hidden toglie il nome della classe...
        ad esempio se la classe Tag ha un attributo __text... il nome dell'attributo sarà _Tag__text
        la funzione toglie _Tag e restituisce __text...
        Se non si tratta di un attributo hidden restituisce il nome stesso senza cambiarlo
        Si suppone che i nomi degli attributi seguano lo standard PIP8 altrimenti ci sono casi in cui potrebbe non funzionare
        :param verbose_param_name: il nome dell'attributo esteso
        :return: una stringa che corrisponde al nome senza la classe di appartenenza
        """
        index = verbose_param_name.find("__")
        return verbose_param_name if index <= 0 else verbose_param_name[index:]

    @staticmethod
    def convert(object_to_convert: object, object_to_convert_name: str, start_tab_num=0) -> str:
        """
        Converte un oggetto nella sua rappresentazione come stringa
        La rappresentazione completa è generata tramite chiamate ricorsive che partono da un oggetto generico sino ad arrivare a stampare
        i valori di tutti gli attributi semplici dell'oggetto stesso...
        :param object_to_convert: oggeto da convertire
        :param object_to_convert_name: nome dell'oggetto da convertire
        :param start_tab_num: numero di tab da usare per identare correttamente gli attributi dell'oggetto
        :return: una stringa che rappresenta tutti i dati dell'oggetto
        """
        if object_to_convert is None:
            return "\n" + (start_tab_num*"\t") + OTS_NONE_COL + object_to_convert_name + OTS_TAGS_COL + " = " + OTS_NONE_COL + "None"

        obj_to_str = ""
        if type(object_to_convert) is str:
            obj_to_str += "\n" + (start_tab_num * "\t") + \
                          OTS_BASIC_TYPE_ATTR_COL + object_to_convert_name + \
                          OTS_BASIC_TYPE_TOKEN_COL + " = " + \
                          OTS_BASIC_TYPE_VALUE_COL + "'" + str(object_to_convert) + "'" + \
                          OTS_BASIC_TYPE_NAME_COL + OTS_CLASS_TAG.format("str")
            return obj_to_str
        elif type(object_to_convert) is int:
            obj_to_str += "\n" + (start_tab_num * "\t") + \
                          OTS_BASIC_TYPE_ATTR_COL + object_to_convert_name + \
                          OTS_BASIC_TYPE_TOKEN_COL + " = " + \
                          OTS_BASIC_TYPE_VALUE_COL + str(object_to_convert) + \
                          OTS_BASIC_TYPE_NAME_COL + OTS_CLASS_TAG.format("int")
            return obj_to_str
        elif type(object_to_convert) is bool:
            obj_to_str += "\n" + (start_tab_num * "\t") + \
                          OTS_BASIC_TYPE_ATTR_COL + object_to_convert_name + \
                          OTS_BASIC_TYPE_TOKEN_COL + " = " + \
                          OTS_BASIC_TYPE_VALUE_COL + str(object_to_convert) + \
                          OTS_BASIC_TYPE_NAME_COL + OTS_CLASS_TAG.format("bool")
            return obj_to_str
        elif type(object_to_convert) is float:
            obj_to_str += "\n" + (start_tab_num * "\t") + \
                          OTS_BASIC_TYPE_ATTR_COL + object_to_convert_name + \
                          OTS_BASIC_TYPE_TOKEN_COL + " = " + \
                          OTS_BASIC_TYPE_VALUE_COL + str(object_to_convert) + \
                          OTS_BASIC_TYPE_NAME_COL + OTS_CLASS_TAG.format("float")
            return obj_to_str
        elif type(object_to_convert) is complex:
            obj_to_str += "\n" + (start_tab_num * "\t") + \
                          OTS_BASIC_TYPE_ATTR_COL + object_to_convert_name + \
                          OTS_BASIC_TYPE_TOKEN_COL + " = " + \
                          OTS_BASIC_TYPE_VALUE_COL + str(object_to_convert) + \
                          OTS_BASIC_TYPE_NAME_COL + OTS_CLASS_TAG.format("complex")
            return obj_to_str
        elif type(object_to_convert) is bytes:
            obj_to_str += "\n" + (start_tab_num * "\t") + \
                          OTS_BASIC_TYPE_ATTR_COL + object_to_convert_name + \
                          OTS_BASIC_TYPE_TOKEN_COL + " = " + \
                          OTS_BASIC_TYPE_VALUE_COL + str(object_to_convert) + \
                          OTS_BASIC_TYPE_NAME_COL + OTS_CLASS_TAG.format("bytes")
            return obj_to_str
        elif type(object_to_convert) is list:
            obj_to_str += "\n" + start_tab_num * "\t" + \
                          OTS_LIST_OBJ_COL + object_to_convert_name + \
                          "\n" + (start_tab_num+1) * "\t" + OTS_LIST_CLASS_COL + OTS_CLASS_TAG.format("list") + \
                          OTS_TAGS_COL + OTS_BEGIN_OBJ_TAG

            for index, elem in enumerate(object_to_convert):
                obj_to_str += start_tab_num * "\t" + \
                              ObjectToStr.convert(elem, OTS_LIST_OBJ_COL + object_to_convert_name +
                                                  OTS_LIST_OBJ_COL + "[" + str(index) + "]", start_tab_num + 2)

            obj_to_str += "\n" + (start_tab_num+1) * "\t" + OTS_LIST_CLASS_COL + OTS_CLASS_TAG.format("list") + \
                          OTS_TAGS_COL + OTS_END_OBJ_TAG
            return obj_to_str
        elif type(object_to_convert) is tuple:
            obj_to_str += "\n" + start_tab_num * "\t" + \
                          OTS_TUPLE_OBJ_COL + object_to_convert_name + \
                          "\n" + (start_tab_num+1) * "\t" + OTS_TUPLE_CLASS_COL + OTS_CLASS_TAG.format("tuple") + \
                          OTS_TAGS_COL + OTS_BEGIN_OBJ_TAG

            for index, elem in enumerate(object_to_convert):
                obj_to_str += start_tab_num * "\t" + \
                              ObjectToStr.convert(elem, OTS_TUPLE_OBJ_COL + object_to_convert_name +
                                                  OTS_TUPLE_OBJ_COL + "[" + str(index) + "]", start_tab_num + 2)

            obj_to_str += "\n" + (start_tab_num+1) * "\t" + OTS_TUPLE_CLASS_COL + OTS_CLASS_TAG.format("tuple") + \
                          OTS_TAGS_COL + OTS_END_OBJ_TAG
            return obj_to_str
        elif type(object_to_convert) is set:
            obj_to_str += "\n" + start_tab_num * "\t" + \
                          OTS_SET_OBJ_COL + object_to_convert_name + \
                          "\n" + (start_tab_num+1) * "\t" + OTS_SET_CLASS_COL + OTS_CLASS_TAG.format("set") + \
                          OTS_TAGS_COL + OTS_BEGIN_OBJ_TAG

            for index, elem in enumerate(object_to_convert):
                obj_to_str += start_tab_num * "\t" + \
                              ObjectToStr.convert(elem, object_to_convert_name +
                                                  OTS_SET_OBJ_COL + "[" + str(index) + "]", start_tab_num + 2)

            obj_to_str += "\n" + (start_tab_num+1) * "\t" + \
                          OTS_SET_CLASS_COL + OTS_CLASS_TAG.format("set") + \
                          OTS_TAGS_COL + OTS_END_OBJ_TAG
            return obj_to_str
        elif type(object_to_convert) is dict:
            obj_to_str += "\n" + start_tab_num * "\t" + \
                          OTS_DICT_OBJ_COL + object_to_convert_name + \
                          "\n" + (start_tab_num+1) * "\t" + OTS_DICT_CLASS_COL + OTS_CLASS_TAG.format("dict") + \
                          OTS_TAGS_COL + OTS_BEGIN_OBJ_TAG

            for key, value in object_to_convert.items():
                if type(key) in (bool, int, float, complex, tuple):
                    key = str(key)
                elif type(key) is str:
                    key = "'" + key + "'"
                else:
                    key = str(key)

                obj_to_str += start_tab_num * "\t" + \
                              ObjectToStr.convert(value, OTS_DICT_OBJ_COL + object_to_convert_name +
                                                  OTS_DICT_OBJ_COL + "[" + key + "]", start_tab_num + 2)

            obj_to_str += "\n" + (start_tab_num+1) * "\t" + \
                          OTS_DICT_CLASS_COL + OTS_CLASS_TAG.format("dict") + \
                          OTS_TAGS_COL + OTS_END_OBJ_TAG
            return obj_to_str
        else:
            obj_to_str += "\n" + start_tab_num * "\t" + \
                          OTS_GENERIC_OBJ_COL + object_to_convert_name + \
                          "\n" + (start_tab_num+1) * "\t" + \
                          OTS_GENERIC_CLASS_COL + OTS_CLASS_TAG.format(object_to_convert.__class__.__name__) + \
                          OTS_TAGS_COL + OTS_BEGIN_OBJ_TAG

            for name, value in list(object_to_convert.__dict__.items()):
                obj_to_str += ObjectToStr.convert(value, ObjectToStr.remove_class_name(name), start_tab_num + 2)

            obj_to_str += "\n" + (start_tab_num+1) * "\t" + \
                          OTS_GENERIC_CLASS_COL + OTS_CLASS_TAG.format(object_to_convert.__class__.__name__) + \
                          OTS_TAGS_COL + OTS_END_OBJ_TAG
            return obj_to_str


if __name__ == '__main__':
    class TestClass:
        pippo = "Pippo"
        pluto = 23

    tc = TestClass()
    print(ObjectToStr.convert(tc, "TestClass"))
