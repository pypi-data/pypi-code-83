from __future__ import annotations # required until python 4.0 in order for a method to be able to return var of type parent class -> https://stackoverflow.com/questions/15853469/putting-current-class-as-return-type-annotation

from typing import Any, Dict, List

def cprint_iter(var: Dict[Any, Any] | List[Any], rec_depth = 0):

    color_list = [
        "\u001b[33m", "\u001b[35m", "\u001b[34m", "\u001b[36m", "\u001b[37m",
        "\u001b[33m", "\u001b[35m", "\u001b[34m", "\u001b[36m", "\u001b[37m",
        "\u001b[33m", "\u001b[35m", "\u001b[34m", "\u001b[36m", "\u001b[37m",
        "\u001b[33m", "\u001b[35m", "\u001b[34m", "\u001b[36m", "\u001b[37m",
        "\u001b[33m", "\u001b[35m", "\u001b[34m", "\u001b[36m", "\u001b[37m",
        "\u001b[33m", "\u001b[35m", "\u001b[34m", "\u001b[36m", "\u001b[37m",
    ]

    def non_iter_print(var):

        if isinstance(var, int) or isinstance(var, float) or isinstance(var, bool):
            col_var = "\033[93m" + str(var) + "\033[0m"
            return col_var

        if isinstance(var, str):
            col_var = "\u001b[34m" + f'"{str(var)}"' + "\033[0m"
            return col_var

        return var

    def get_iter_pair(iterable):
        return iterable.items() if isinstance(iterable, dict) else enumerate(iterable)

    op_br = color_list[rec_depth] + "{" + "\033[0m"
    cl_br = color_list[rec_depth] + "}" + "\033[0m"
    spacing = "  " * rec_depth
    # for k, v in get_iter_pair(var):
    for k, v in get_iter_pair(var):
        col_k = spacing + "\u001b[32m" + str(k) + "\033[0m" + ": "

        if isinstance(v, dict) or isinstance(v, list):
        # if isinstance(v, dict):
            rec_depth += 1
            print(col_k, end=f"{op_br}")
            if v:
                print()
                cprint_iter(v, rec_depth)
                print(spacing + cl_br)
            else:
                print(cl_br)
            rec_depth -= 1
        else:
            formatted_v = non_iter_print(v)
            print(col_k, end="")
            print(formatted_v)
