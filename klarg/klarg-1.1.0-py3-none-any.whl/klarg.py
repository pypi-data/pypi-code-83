import sys
from typing import Callable, Union

# Some information about this package
__version__ = "1.1.0"

# All the command line arguments
ALL_ARGS = sys.argv[1: len(sys.argv)]

# The configuration settings, this can be changed with the config function
CONFIG = {
    "needs_short_flags": False,
    "long_prefix": "--",
    "short_prefix": "-",
    "help_flag": ("--help", "-h"),
    "version_flag": ("--version", "-v")
}

"""
Here is a list of all the base functions
"""


def base_exists(name: str, args_list: list) -> bool:
    return name in args_list


def base_get_all(args_list: list) -> list:  # bigoof
    return args_list


def base_get_bool(
    name: str,
    args_list: list,
    short: str = "default-str"
) -> bool:
    long_name = CONFIG["long_prefix"] + name
    short_name = CONFIG["short_prefix"] + short

    if short == "default-short":
        if (CONFIG["needs_short_flags"]):
            raise Exception(
                "No short flag for get_bool()"
            )

        else:
            if base_exists(long_name, args_list):
                return True

            else:
                return False
    else:
        if base_exists(long_name, args_list):
            return True

        if base_exists(short_name, args_list):
            return True

        else:
            return False


def base_on_help(action: Callable, args_list: list) -> None:
    """
    `action: function: NEEDED`

    The `action` is run when klarg detects the help flag.
    What klarg looks for can be configured in `CONFIG`
    with the option `"help_flag"`.

    Example:
    ```py
    # docs_example.py
    import klarg
    def display_help_message():
        print("Here you go")

    klarg.on_help(display_help_message)

    # python docs_example.py --help
    # Here you go
    ```

    """

    long_help, short_help = CONFIG["help_flag"]

    if base_exists(long_help, args_list):
        action()

    if base_exists(short_help, args_list):
        action()


def base_on_version(message: str, args_list: list) -> None:
    """
    `message: str: NEEDED`

    Klarg displays the `message` when the version flag is detected.
    What klarg looks for can be configured in `CONFIG`
    with the option `"version_flag"`.

    Example:
    ```py
    # docs_example.py
    import klarg
    klarg.project_version("This project version is 1.2.3")

    # python docs_example.py --version
    # This project version is 1.2.3
    ```

    """

    long_version, short_version = CONFIG["version_flag"]

    if exists(long_version) or exists(short_version):
        print(message)

    if base_exists(short_version, args_list):
        print(message)


def base_get_str(
    name: str,
    args_list: list,
    short: str = "default-short",
    on_error: dict = {}
) -> Union[str, None]:
    """
    `name: str: NEEDED`

    `short: str: optional`

    `on_error: function: optional`

    `get_str` is a function that collects a `name`,
     which is the multi letter flag, a `short`, which is the
     shortened version of the flag. There is only one type of
     errors it can encounter, which is when no value is provided.
     Because of this, `on_error` is not a dictionary,
     but a special function that handles when no value is provided.

    Example:
    ```py
    # docs_example.py
    import klarg
    def handle_error_none():
        print(f"No values provided")

    some_str = klarg.get_str("--some-str", "-s", on_error=handle_error_none)

    print(f"{some_str} is cool")

    # python docs_example.py --some-str
    # No values provided

    # python docs_example.py -s "klarg"
    # klarg is cool
    ```

    """

    long_name = CONFIG["long_prefix"] + name
    short_name = CONFIG["short_prefix"] + short

    # Checks if a given argument is a value or not.
    def is_valid_value(arg: str) -> bool:
        # Makes sure it is not a multi letter flag
        if arg.startswith(CONFIG["long_prefix"]):
            return False

        # Makes sure it is not a short flag
        if arg.startswith(CONFIG["short_prefix"]):
            return False

        # Makes sure it is not part of the version or help flags
        if (arg in CONFIG["version_flag"]) or (arg in CONFIG["help_flag"]):
            return False
        else:
            return True

    # Default handling for ERR_NONE
    def default_handle_none():
        print(f"ERR_NONE: There is no value provided for {long_name}")
        exit(1)

    # Default handling for ERR_MUL
    def default_handle_mul():
        print(f"ERR_MUL: There are multiple values provided for {long_name}")
        exit(1)

    def is_key(key, dict: dict) -> bool:
        if key in dict.keys():
            return True
        else:
            return False

    non_existent_long_name = not base_exists(long_name, args_list)
    non_existent_short_name = not base_exists(short_name, args_list)

    # Does not exist in command line args
    if non_existent_long_name and non_existent_short_name:
        return None

    # Configure error_handling
    if not is_key("ERR_NONE", on_error):
        on_error["ERR_NONE"] = default_handle_none

    if not is_key("ERR_MUL", on_error):
        on_error["ERR_MUL"] = default_handle_mul

    # ERR_NONE
    # Ther cannot be enough space for the argument and
    # it's value
    if len(ALL_ARGS) < 2:
        on_error["ERR_NONE"]()

    # ERR_MUL
    # If there is more than one occurence of short_name or long_name
    if (args_list.count(long_name) > 1) or (args_list.count(short_name) > 1):
        on_error["ERR_MUL"]()

    # ERR_MUL
    # if both short and long arguments exists
    long_args_exists = base_exists(long_name, args_list)
    short_args_exists = base_exists(short_name, args_list)

    if long_args_exists and short_args_exists:
        on_error["ERR_MUL"]()

    # Gets the next value of the given flag
    def get_next_value(flag: str) -> str:
        index_point = args_list.index(flag)

        next_value = args_list[(index_point + 1)]

        if (is_valid_value(next_value)):
            return next_value

        else:  # ERR_NONE
            # If there is no argument passed to
            # long_args
            on_error["ERR_NONE"]()

    if short == "default-short":
        if (CONFIG["needs_short_flags"]):
            raise Exception(
                f"No short flag for {long_name}"
            )
        else:
            return get_next_value(long_name)
    else:
        if base_exists(long_name, args_list):
            return get_next_value(long_name)

        elif base_exists(short_name, args_list):
            return get_next_value(short_name)

        else:  # If it does not exist
            return None


def base_get_num(
    name: str,
    args_list: dict,
    short: str = "default-short",
    on_error: dict = {},
) -> Union[int, float, None]:

    def is_key(key, dict: dict) -> bool:
        if key in dict.keys():
            return True
        else:
            return False

    def to_num(string: str) -> Union[int, float, str]:
        if "." in string:
            return float(string)
        else:
            try:
                return int(string)
            except ValueError:
                return string

    # Default handling for ERR_NUM
    def default_handle_num(value):
        print(f"ERR_NUM: \"{value}\" is not a number")
        exit(1)

    if not is_key("ERR_NUM", on_error):
        on_error["ERR_NUM"] = default_handle_num

    value = base_get_str(
        name=name,
        short=short,
        on_error=on_error,
        args_list=ALL_ARGS
    )

    num = to_num(value)

    if type(num) == str:
        on_error["ERR_NUM"](value)
    else:
        return num


"""
-------------------------------------------- KLARG BASIC
"""


def exists(name: str) -> bool:
    """
    `name: str: NEEDED`

    Checks if the `name` exists in the list of command line arguments given,
    this was designed to be an internal function for making things more
    readable, but then I realized that it could potentially be helpful.

    Example:
    ```py
    # docs_example.py
    import klarg

    something_exists = klarg.exists("something")
    if something_exists:
        print("Something exists")
    else:
        print("Nothing exists (that's kind of dark)")

    # python docs_example.py does something exist
    # Something exists

    # python docs_example.py does nothing exist
    # Nothing exists (that's kind of dark)
```

    """

    return base_exists(name=name, args_list=ALL_ARGS)


def get_all() -> list:
    """
    Collects all the arguments passed and returns them all as a tuple
    full of strings. This is useful when a program needs to collect
    a list of all the arguments passed on to operate on,
    it passes everything single option passed to the file

    Example:
`   ```py
    # docs_example.py
    import klarg

    all_args = klarg.get_all()
    print(f"All args {all_args}")

    # python docs_example.py -a -b "c" -d --efgh --ijklmn 0
    # All args ("-a", "-b", "c", "-d", "--efgh", "--ijklmn", "0")
    ```

    """

    return ALL_ARGS


def get_bool(name: str, short: str = "default-short") -> bool:
    """
    `name: str: NEEDED`

    `short: str: optional`

    `get_bool` is a function that collects `name`, a string, and `short`,
    also a string. `name` is the long name for the command line argument,
    i.e. (`--long-name`). `short` is the shorter name for the command
    line argument (`-s`). Normally, if `short` is not given,
    then it will not raise an error, unless `"needs_short_flags"`
    is set to `True` in `CONFIG`.

    Example:
    ```py
    # docs_example.py
    import klarg

    is_there = klarg.bool("--is-there", "-i")

    if (is_there):
        print("Is there")
    else:
        print("Is not there")

    # python docs_example.py
    # Is not there

    # python docs_example.py --is-there
    # is there
    ```

    """

    return base_get_bool(
        name=name,
        short=short,
        args_list=ALL_ARGS
    )


def on_help(action: Callable) -> None:
    """
    `action: function: NEEDED`

    The `action` is run when klarg detects the help flag.
    What klarg looks for can be configured in `CONFIG`
    with the option `"help_flag"`.

    Example:
    ```py
    # docs_example.py
    import klarg
    def display_help_message():
        print("Here you go")

    klarg.on_help(display_help_message)

    # python docs_example.py --help
    # Here you go
    ```

    """

    return base_on_help(
        action=action,
        args_list=ALL_ARGS
    )


def on_version(message: str) -> None:
    """
    `message: str: NEEDED`

    Klarg displays the `message` when the version flag is detected.
    What klarg looks for can be configured in `CONFIG`
    with the option `"version_flag"`.

    Example:
    ```py
    # docs_example.py
    import klarg
    klarg.project_version("This project version is 1.2.3")

    # python docs_example.py --version
    # This project version is 1.2.3
    ```

    """

    return base_on_version(
        message=message,
        args_list=ALL_ARGS
    )


def get_str(
    name: str,
    short: str = "default-short",
    on_error: dict = {}
) -> Union[str, None]:
    """
    `name: str: NEEDED`

    `short: str: optional`

    `on_error: function: optional`

    `get_str` is a function that collects a `name`,
     which is the multi letter flag, a `short`, which is the
     shortened version of the flag. There is only one type of
     errors it can encounter, which is when no value is provided.
     Because of this, `on_error` is not a dictionary,
     but a special function that handles when no value is provided.

    Example:
    ```py
    # docs_example.py
    import klarg
    def handle_error_none():
        print(f"No values provided")

    some_str = klarg.get_str("--some-str", "-s", on_error=handle_error_none)

    print(f"{some_str} is cool")

    # python docs_example.py --some-str
    # No values provided

    # python docs_example.py -s "klarg"
    # klarg is cool
    ```

    """

    return base_get_str(
        name=name,
        short=short,
        on_error=on_error,
        args_list=ALL_ARGS
    )


def get_num(
    name: str,
    short: str = "default-short",
    on_error: dict = {}
) -> Union[int, float, None]:
    """
    `name: str: NEEDED`

    `short: str: optional`

    `on_error: dict: optional`

    `get_num` is a function that collects a `name`,
    which is the multi letter flag, a `short`,
    which is the shortened version of the flag.
    There are two possible types of errors it can encounter,
    one being that the value it got was not a number, it did not
    get a value at all, or that there are multiple declarations of that flag.
    he error names are `ERR_NUM`, `ERR_NONE` and `ERR_MUL` respectively.
    `on_error` is a dictionary, all three keys,
    `ERR_NUM`,`ERR_NONE` and `ERR_MUL` are not all needed,
    because there is default handling for those types of errors.
    However, if there is no flag with the name of `name`,
    then `get_num` returns None.

    Example:
    ```py
    # docs_example.py
    import klarg
    def handle_error_num(value):
        print(f"{value} is not a number")

    def handle_error_none():
        print("No values provided")

    error_handlers = {
        "ERR_NUM": handle_error_num(),
        "ERR_NONE": handle_error_none()
    }

    number_something = klarg.get_num(
        name="--number-something",
        short="-n", on_error=error_handlers
        )
    print(f"The suprise number is {number_something}")

    # python docs_example.py -n 1a
    # 1a is not a number

    # python docs_example.py -n
    # No values provided

    # python docs_example.py -n 12345
    # The suprise number is 12345
    ```

    """

    return base_get_num(
        name=name,
        short=short,
        on_error=on_error,
        args_list=ALL_ARGS
    )


class command():
    """
    `name: str: NEEDED`

    This creates a class with the command line that has the functions
    `project_version()`, `on_help()`, `get_num()`, `get_str()`,
    `get_bool()`, and `get_all()`. The only difference is that
    the arguments are parsed after the declaration of the command.
    This means that if you have a list of command line arguments
    `["-f", "reply", "-n", "12", "example.txt"]`,
    and the command name is `reply`. The available command line arguments
    are `["-n", "12", "example.txt"]`
    """

    def __init__(self, name: str):
        beginning_index = ALL_ARGS.index(name) + 1
        self.all_arguments = ALL_ARGS[beginning_index: len(ALL_ARGS)]

    def exists(self, name: str) -> bool:
        """
        `name: str: NEEDED`

        Checks if the `name` exists in the list of command line
        arguments given, this was designed to be an
        internal function for making things more readable, but then
        I realized that it could potentially be helpful.

        Example:
        ```py
        # docs_example.py
        import klarg

        something_exists = klarg.exists("something")
        if something_exists:
            print("Something exists")
        else:
            print("Nothing exists (that's kind of dark)")

        # python docs_example.py does something exist
        # Something exists

        # python docs_example.py does nothing exist
        # Nothing exists (that's kind of dark)
    ```

        """

        return base_exists(name=name, args_list=self.all_arguments)

    def get_all(self) -> list:
        """
        Collects all the arguments passed and returns them all as a tuple
        full of strings. This is useful when a program needs to collect
        a list of all the arguments passed on to operate on,
        it passes everything single option passed to the file

        Example:
    `   ```py
        # docs_example.py
        import klarg

        all_args = klarg.get_all()
        print(f"All args {all_args}")

        # python docs_example.py -a -b "c" -d --efgh --ijklmn 0
        # All args ("-a", "-b", "c", "-d", "--efgh", "--ijklmn", "0")
        ```

        """

        return base_get_all(self.all_arguments)

    def get_bool(self, name: str, short: str = "default-short") -> bool:
        """
        `name: str: NEEDED`

        `short: str: optional`

        `get_bool` is a function that collects `name`, a string, and `short`,
        also a string. `name` is the long name for the command line argument,
        i.e. (`--long-name`). `short` is the shorter name for the command
        line argument (`-s`). Normally, if `short` is not given,
        then it will not raise an error, unless `"needs_short_flags"`
        is set to `True` in `CONFIG`.

        Example:
        ```py
        # docs_example.py
        import klarg

        is_there = klarg.bool("--is-there", "-i")

        if (is_there):
            print("Is there")
        else:
            print("Is not there")

        # python docs_example.py
        # Is not there

        # python docs_example.py --is-there
        # is there
        ```

        """

        return base_get_bool(
            name=name,
            short=short,
            args_list=self.all_arguments
        )

    def on_help(self, action: Callable) -> None:
        """
        `action: function: NEEDED`

        The `action` is run when klarg detects the help flag.
        What klarg looks for can be configured in `CONFIG`
        with the option `"help_flag"`.

        Example:
        ```py
        # docs_example.py
        import klarg
        def display_help_message():
            print("Here you go")

        klarg.on_help(display_help_message)

        # python docs_example.py --help
        # Here you go
        ```

        """

        return base_on_help(
            action=action,
            args_list=self.all_arguments
        )

    def on_version(self, message: str) -> None:
        """
        `message: str: NEEDED`

        Klarg displays the `message` when the version flag is detected.
        What klarg looks for can be configured in `CONFIG`
        with the option `"version_flag"`.

        Example:
        ```py
        # docs_example.py
        import klarg
        klarg.project_version("This project version is 1.2.3")

        # python docs_example.py --version
        # This project version is 1.2.3
        ```

        """

        return base_on_version(
            message=message,
            args_list=self.all_arguments
        )

    def get_str(
        self,
        name: str,
        short: str = "default-short",
        on_error: dict = {}
    ) -> Union[str, None]:
        """
        `name: str: NEEDED`

        `short: str: optional`

        `on_error: function: optional`

        `get_str` is a function that collects a `name`,
         which is the multi letter flag, a `short`, which is the
         shortened version of the flag. There is only one type of
         errors it can encounter, which is when no value is provided.
         Because of this, `on_error` is not a dictionary,
         but a special function that handles when no value is provided.

        Example:
        ```py
        # docs_example.py
        import klarg
        def handle_error_none():
            print(f"No values provided")

        some_str = klarg.get_str(
            "--some-str",
            "-s",
            on_error=handle_error_none
            )

        print(f"{some_str} is cool")

        # python docs_example.py --some-str
        # No values provided

        # python docs_example.py -s "klarg"
        # klarg is cool
        ```

        """

        return base_get_str(
            name=name,
            short=short,
            on_error=on_error,
            args_list=self.all_arguments
        )

    def get_num(
        self,
        name: str,
        short: str = "default-short",
        on_error: dict = {}
    ) -> Union[int, float, None]:
        """
        `name: str: NEEDED`

        `short: str: optional`

        `on_error: dict: optional`

        `get_num` is a function that collects a `name`,
        which is the multi letter flag, a `short`,
        which is the shortened version of the flag.
        There are two possible types of errors it can encounter,
        one being that the value it got was not a number, it did not
        get a value at all, or that there are multiple declarations of that
        flag. he error names are `ERR_NUM`, `ERR_NONE` and `ERR_MUL`
        respectively. `on_error` is a dictionary, all three keys,
        `ERR_NUM`,`ERR_NONE` and `ERR_MUL` are not all needed,
        because there is default handling for those types of errors.
        However, if there is no flag with the name of `name`,
        then `get_num` returns None.

        Example:
        ```py
        # docs_example.py
        import klarg
        def handle_error_num(value):
            print(f"{value} is not a number")

        def handle_error_none():
            print("No values provided")

        error_handlers = {
            "ERR_NUM": handle_error_num(),
            "ERR_NONE": handle_error_none()
        }

        number_something = klarg.get_num(
            name="--number-something",
            short="-n", on_error=error_handlers
            )
        print(f"The suprise number is {number_something}")

        # python docs_example.py -n 1a
        # 1a is not a number

        # python docs_example.py -n
        # No values provided

        # python docs_example.py -n 12345
        # The suprise number is 12345
        ```

        """

        return base_get_num(
            name=name,
            short=short,
            on_error=on_error,
            args_list=self.all_arguments
        )
