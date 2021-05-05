#!/usr/bin/env python3


"""
La classe ColTex (abbreviazione di ColoredText) è stata pensate per facilitare la creazione di output colorato su stdout
"""


__author__ = "Stefano Gigli"
__copyright__ = "Copyright 2019, SG Software"
__credits__ = []
__license__ = "GPL"
__version__ = "0.9"
__maintainer__ = "Stefano Gigli"
__email__ = "exe.dev.exe@gmail.com"
__status__ = "Beta version"


class ColTex:
    class ForegroundColor:
        WHITE = '\033[30m'
        RED = '\033[31m'
        GREEN = '\033[32m'
        ORANGE = '\033[33m'
        BLUE = '\033[34m'
        PURPLE = '\033[35m'
        CYAN = '\033[36m'
        LIGHT_GRAY = '\033[37m'

        GRAY = '\033[90m'
        LIGHT_RED = '\033[91m'
        LIGHT_GREEN = '\033[92m'
        YELLOW = '\033[93m'
        LIGHT_BLUE = '\033[94m'
        PINK = '\033[95m'
        LIGHT_CYAN = '\033[96m'

    class BackgroundColors:
        BLACK = '\033[40m'
        RED = '\033[41m'
        GREEN = '\033[42m'
        ORANGE = '\033[43m'
        BLUE = '\033[44m'
        PURPLE = '\033[45m'
        CYAN = '\033[46m'
        LIGHT_GRAY = '\033[47m'
        TRANSPARENT = ""

    class Modifiers:
        RESET = '\033[0m'
        BOLD = '\033[01m'
        DISABLE = '\033[02m'
        UNDERLINE = '\033[04m'
        REVERSE = '\033[07m'
        STRIKE_THROUGH = '\033[09m'
        INVISIBLE = '\033[08m'

    @staticmethod
    def colorize(text, foreground_color, background_color=BackgroundColors.TRANSPARENT,
                 bold=False, disable=False, underline=False, reverse=False, strike_through=False, invisible=False) -> str:
        return foreground_color + \
               background_color + \
               (ColTex.Modifiers.BOLD if bold else "") + \
               (ColTex.Modifiers.DISABLE if disable else "") + \
               (ColTex.Modifiers.UNDERLINE if underline else "") + \
               (ColTex.Modifiers.REVERSE if reverse else "") + \
               (ColTex.Modifiers.STRIKE_THROUGH if strike_through else "") + \
               (ColTex.Modifiers.INVISIBLE if invisible else "") + \
               text + \
               ColTex.Modifiers.RESET

    @staticmethod
    def red(text, background_color=BackgroundColors.TRANSPARENT,
            bold=False, disable=False, underline=False, reverse=False, strike_through=False, invisible=False) -> str:
        return ColTex.colorize(text, ColTex.ForegroundColor.RED, background_color=background_color,
                               bold=bold, disable=disable, underline=underline,
                               reverse=reverse, strike_through=strike_through, invisible=invisible)

    @staticmethod
    def green(text, background_color=BackgroundColors.TRANSPARENT,
              bold=False, disable=False, underline=False, reverse=False, strike_through=False, invisible=False) -> str:
        return ColTex.colorize(text, ColTex.ForegroundColor.GREEN, background_color=background_color,
                               bold=bold, disable=disable, underline=underline,
                               reverse=reverse, strike_through=strike_through, invisible=invisible)

    @staticmethod
    def orange(text, background_color=BackgroundColors.TRANSPARENT,
               bold=False, disable=False, underline=False, reverse=False, strike_through=False, invisible=False) -> str:
        return ColTex.colorize(text, ColTex.ForegroundColor.ORANGE, background_color=background_color,
                               bold=bold, disable=disable, underline=underline,
                               reverse=reverse, strike_through=strike_through, invisible=invisible)

    @staticmethod
    def blue(text, background_color=BackgroundColors.TRANSPARENT,
             bold=False, disable=False, underline=False, reverse=False, strike_through=False, invisible=False) -> str:
        return ColTex.colorize(text, ColTex.ForegroundColor.BLUE, background_color=background_color,
                               bold=bold, disable=disable, underline=underline,
                               reverse=reverse, strike_through=strike_through, invisible=invisible)

    @staticmethod
    def purple(text, background_color=BackgroundColors.TRANSPARENT,
               bold=False, disable=False, underline=False, reverse=False, strike_through=False, invisible=False) -> str:
        return ColTex.colorize(text, ColTex.ForegroundColor.PURPLE, background_color=background_color,
                               bold=bold, disable=disable, underline=underline,
                               reverse=reverse, strike_through=strike_through, invisible=invisible)

    @staticmethod
    def cyan(text, background_color=BackgroundColors.TRANSPARENT,
             bold=False, disable=False, underline=False, reverse=False, strike_through=False, invisible=False) -> str:
        return ColTex.colorize(text, ColTex.ForegroundColor.CYAN, background_color=background_color,
                               bold=bold, disable=disable, underline=underline,
                               reverse=reverse, strike_through=strike_through, invisible=invisible)

    @staticmethod
    def light_gray(text, background_color=BackgroundColors.TRANSPARENT,
                   bold=False, disable=False, underline=False, reverse=False, strike_through=False, invisible=False) -> str:
        return ColTex.colorize(text, ColTex.ForegroundColor.LIGHT_GRAY, background_color=background_color,
                               bold=bold, disable=disable, underline=underline,
                               reverse=reverse, strike_through=strike_through, invisible=invisible)

    @staticmethod
    def gray(text, background_color=BackgroundColors.TRANSPARENT,
             bold=False, disable=False, underline=False, reverse=False, strike_through=False, invisible=False) -> str:
        return ColTex.colorize(text, ColTex.ForegroundColor.GRAY, background_color=background_color,
                               bold=bold, disable=disable, underline=underline,
                               reverse=reverse, strike_through=strike_through, invisible=invisible)

    @staticmethod
    def light_red(text, background_color=BackgroundColors.TRANSPARENT,
                  bold=False, disable=False, underline=False, reverse=False, strike_through=False, invisible=False) -> str:
        return ColTex.colorize(text, ColTex.ForegroundColor.LIGHT_RED, background_color=background_color,
                               bold=bold, disable=disable, underline=underline,
                               reverse=reverse, strike_through=strike_through, invisible=invisible)

    @staticmethod
    def light_green(text, background_color=BackgroundColors.TRANSPARENT,
                    bold=False, disable=False, underline=False, reverse=False, strike_through=False, invisible=False) -> str:
        return ColTex.colorize(text, ColTex.ForegroundColor.LIGHT_GREEN, background_color=background_color,
                               bold=bold, disable=disable, underline=underline,
                               reverse=reverse, strike_through=strike_through, invisible=invisible)

    @staticmethod
    def yellow(text, background_color=BackgroundColors.TRANSPARENT,
               bold=False, disable=False, underline=False, reverse=False, strike_through=False, invisible=False) -> str:
        return ColTex.colorize(text, ColTex.ForegroundColor.YELLOW, background_color=background_color,
                               bold=bold, disable=disable, underline=underline,
                               reverse=reverse, strike_through=strike_through, invisible=invisible)

    @staticmethod
    def light_blue(text, background_color=BackgroundColors.TRANSPARENT,
                   bold=False, disable=False, underline=False, reverse=False, strike_through=False, invisible=False) -> str:
        return ColTex.colorize(text, ColTex.ForegroundColor.LIGHT_BLUE, background_color=background_color,
                               bold=bold, disable=disable, underline=underline,
                               reverse=reverse, strike_through=strike_through, invisible=invisible)

    @staticmethod
    def pink(text, background_color=BackgroundColors.TRANSPARENT,
             bold=False, disable=False, underline=False, reverse=False, strike_through=False, invisible=False) -> str:
        return ColTex.colorize(text, ColTex.ForegroundColor.PINK, background_color=background_color,
                               bold=bold, disable=disable, underline=underline,
                               reverse=reverse, strike_through=strike_through, invisible=invisible)

    @staticmethod
    def light_cyan(text, background_color=BackgroundColors.TRANSPARENT,
                   bold=False, disable=False, underline=False, reverse=False, strike_through=False, invisible=False) -> str:
        return ColTex.colorize(text, ColTex.ForegroundColor.LIGHT_CYAN, background_color=background_color,
                               bold=bold, disable=disable, underline=underline,
                               reverse=reverse, strike_through=strike_through, invisible=invisible)


if __name__ == '__main__':
    print(ColTex.red("Questo va in rosso", underline=True, background_color=ColTex.BackgroundColors.CYAN, bold=True))
    print(ColTex.orange("orange", bold=True))
    print(ColTex.light_red("light red", strike_through=True, background_color=ColTex.BackgroundColors.BLUE))
    print(ColTex.red("red", invisible=True, reverse=True))
