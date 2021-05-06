# -*- coding: UTF-8 -*-
__author__ = 'Aki Mäkinen'
import shutil
import textwrap

from colorama import Fore, Style

class State:
    def __init__(self):
        self.errors = {}
        self.suspicions = {}


class StatefulLogger:
    def __init__(self, indent=0, level=0, state=State()):
        self.indent = indent
        self.level = level
        self.state = state

    def __log(self, msg, color, *, level=None):
        if level is None:
            level = self.level
        terminal_size = shutil.get_terminal_size((120, 20))
        width = max(int(terminal_size.columns / 2), 120)  # Because.... Hervantavakiot?
        indent = " " * self.indent * level
        wrapper = textwrap.TextWrapper(width=width, initial_indent=indent, subsequent_indent=indent)

        msg = wrapper.fill(color + msg + Style.RESET_ALL)
        print(msg)

    def info(self, *args):
        msg = ", ".join(args)
        self.__log(msg, Fore.LIGHTBLUE_EX)

    def warn(self, *args, source_id=None):
        if source_id is None:
            print("Logger id cannot be None")
            exit(1)

        msg = ", ".join(args)

        if source_id not in self.state.suspicions:
            self.state.suspicions[source_id] = []
        self.state.suspicions[source_id].append(msg)

        self.__log(msg, Fore.LIGHTYELLOW_EX)

    def error(self, *args, source_id=None):
        print("Call")
        if source_id is None:
            print("Logger id cannot be None")
            exit(1)

        msg = ", ".join(args)

        if source_id not in self.state.errors:
            self.state.errors[source_id] = []
        self.state.errors[source_id].append(msg)

        self.__log(msg, Fore.LIGHTRED_EX)

    def summary(self, **kwargs):
        print(f"""
************************************************************************************************************************
SUMMARY ({kwargs.get('filename', '')})        
************************************************************************************************************************
""")

        print(f"SUSPICIONS ({sum([len(v) for v in self.state.suspicions.values()])}):\n")
        for logger_id, msgs in self.state.suspicions.items():
            self.__log(logger_id + ":", Fore.LIGHTYELLOW_EX, level=0)
            for msg in msgs:
                self.__log("\u2600 " + msg, Fore.LIGHTYELLOW_EX, level=1)

        print("------------------------\n")

        print(f"ERRORS ({ sum([len(v) for v in self.state.errors.values()]) }):\n")
        for logger_id, msgs in self.state.errors.items():
            self.__log(logger_id + ":", Fore.LIGHTRED_EX, level=0)
            for msg in msgs:
                self.__log("\u2600 " + msg, Fore.LIGHTRED_EX, level=1)

    def reset_state(self):
        self.state = State()
        self.state.errors = {}
        self.state.suspicions = {}

    def new(self):
        return StatefulLogger(
            indent=self.indent,
            level=self.level + 1,
            state=self.state
        )
