import re
import traceback


class HKSError(Exception):
    "The exception is raised by failures in the hks python modulesystem."
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
    
    def __str__(self):
        e = super().__str__()

        tb = traceback.format_exception(etype=type(self), value=super(), tb=self.__traceback__)

        pattern = r"(^\s+)"
        tb = re.sub(pattern, "", tb[-2].split("\n")[0])

        e_with_tb = "{} ({}).".format(e, tb)

        return e_with_tb

    def __repr__(self) -> str:
        return str(self)


class HTypeError(TypeError, HKSError):
    "The exception is raised when a variable/object/... has wrong type."
    def __init__(self, obj_name: str, obj: object, *args) -> None:
        notification = "The parameter {} expected".format(obj_name)
        for i, arg in enumerate(args):
            if i > 0:
                notification += " or"
            else:
                notification += " the"

            if type(arg).__name__ == "type":
                notification += " {}".format(arg.__name__)
            else:
                notification += " {}".format(arg)

        notification += ", but got the {}.".format(type(obj).__name__)
        HKSError.__init__(self, notification)


class HFormatError(HKSError):
    "The exception is raised when a variable/function/.. has wrong format."
