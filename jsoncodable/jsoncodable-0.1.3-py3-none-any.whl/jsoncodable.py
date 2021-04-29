# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# System
from typing import Optional, Dict, Any, Union
import json, os, io, gzip

# Pip
from noraise import noraise
import jsonpickle

# -------------------------------------------------------------------------------------------------------------------------------- #



# ------------------------------------------------------------ Defines ----------------------------------------------------------- #

GZIP_EXTENSION = '.gz'

# -------------------------------------------------------------------------------------------------------------------------------- #



# ------------------------------------------------------ class: JsonCodable ------------------------------------------------------ #

class JSONCodable:

    # --------------------------------------------------- Public properties -------------------------------------------------- #

    @property
    def dict(self) -> Dict[str, Any]:
        '''Creates, dict from object.'''
        return self.to_dict(self, recursive=False)

    @property
    def json(self) -> Dict[str, Any]:
        '''Same as .dict, but converts all object values to JSONSerializable ones recursively'''
        return json.loads(jsonpickle.encode(self))


    # ---------------------------------------------------- Public methods ---------------------------------------------------- #

    def jsonstr(
        self,
        unpicklable: bool = True,
        indent: Optional[int] = None,
    ) -> str:
        '''Same as .json, but json encoded string'''
        return jsonpickle.encode(self, unpicklable=unpicklable, indent=indent)

    def save_to_file(
        self,
        path: str,
        indent: Optional[int] = 4,
        gzipped: bool = False
    ) -> str:
        if gzipped:
            if not path.endswith(GZIP_EXTENSION):
                path += GZIP_EXTENSION
                print('added ".gz" to the path so it will be "{}"'.format(path))

            if indent == 4:
                indent = None

            with gzip.open(path, 'wb') as f:
                f.write(
                    self.jsonstr(
                        unpicklable=True,
                        indent=indent
                    ).encode('utf-8')
                ) 
        else:
            with open(path, 'w') as f:
                json.dump(self.json, f, indent=indent)

        return path

    # alias
    save = save_to_file

    @classmethod
    @noraise()
    def from_json(
        cls,
        json_file_or_json_file_path_or_json_str_or_dict: Union[
            Union[io.TextIOBase, io.BufferedIOBase, io.RawIOBase, io.IOBase],
            str,
            Dict[str, Any]
        ]
    ) -> Optional:
        return jsonpickle.decode(cls.__get_patched_json_str(json_file_or_json_file_path_or_json_str_or_dict))

    # aliases
    load = from_json
    from_json_file = from_json

    def printjson(
        self,
        unpicklable: bool = False,
        indent: Optional[int] = 4,
    ) -> None:
        print(
            self.jsonstr(
                unpicklable=unpicklable,
                indent=indent
            )
        )

    #alias
    jsonprint = printjson

    @classmethod
    def to_dict(cls, obj: Optional[Any], recursive: bool=True) -> Optional[Dict[str, Any]]:
        return json.loads(jsonpickle.encode(obj)) if recursive else cls.__real__dict__(obj, include_private=False)

    @classmethod
    def full_class_name(cls):
        module = cls.__module__

        if module == '__builtin__':
            return cls.__name__

        return module + '.' + cls.__name__

    # ---------------------------------------------------- Private methods --------------------------------------------------- #

    @classmethod
    @noraise()
    def __get_patched_json_str(
        cls,
        json_file_or_json_file_path_or_json_str_or_dict: Union[
            Union[io.TextIOBase, io.BufferedIOBase, io.RawIOBase, io.IOBase],
            str,
            Dict[str, Any]
        ]
    ) -> Optional[str]:
        d = cls.__get_dict(json_file_or_json_file_path_or_json_str_or_dict)
        d['py/object'] = cls.full_class_name()

        return json.dumps(d)

    @classmethod
    def __get_dict(
        cls,
        json_file_or_json_file_path_or_json_str_or_dict: Union[
            Union[io.TextIOBase, io.BufferedIOBase, io.RawIOBase, io.IOBase],
            str,
            Dict[str, Any]
        ]
    ) -> Dict[str, Any]:
        var = json_file_or_json_file_path_or_json_str_or_dict

        if isinstance(var, str):
            # json string, json file path, gzipped json file path
            possile_path = var
            path_exists = False

            if os.path.exists(possile_path):
                path_exists = True
            else:
                possile_path += GZIP_EXTENSION
            
            if path_exists or os.path.exists(possile_path):
                # json file path, gzipped json file path
                path = possile_path
                open_method = gzip.open if cls.__is_gz_path(path) else open

                with open_method(path, 'rb') as f:
                    return json.load(f)
            else:
                # json str
                return json.loads(var)

        if (
            isinstance(var, io.TextIOBase)
            or
            isinstance(var, io.BufferedIOBase)
            or
            isinstance(var, io.RawIOBase)
            or
            isinstance(var, io.IOBase)
        ):
            # file
            return json.load(var)

        return var
    
    @classmethod
    def __is_gz_path(
        cls,
        path: str
    ) -> bool:
        with open(path, 'rb') as f:
            return cls.__is_gz_file(f)

    @staticmethod
    def __is_gz_file(file) -> bool:
        return file.read(2) == b'\x1f\x8b'

    @staticmethod
    def __real__dict__(obj, include_private: bool = False) -> Dict[str, Any]:
        object_dict = {}

        for method_name in [method_name for method_name in dir(obj)]:
            if (
                (
                    not include_private and method_name.startswith('_')
                )
                or
                (
                    method_name in dir(JSONCodable())
                )
                or
                (
                    callable(getattr(obj, method_name))
                )
            ):
                continue

            object_dict[method_name] = getattr(obj, method_name)

        return object_dict


# -------------------------------------------------------------------------------------------------------------------------------- #