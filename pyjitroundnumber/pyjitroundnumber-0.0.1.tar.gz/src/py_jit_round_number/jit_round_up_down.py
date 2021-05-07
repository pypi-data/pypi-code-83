import math


class JitRoundNumber:

    def __init__( self, number: float, decimals: int = 4 ):
        self.number = number
        self.decimals = decimals
        self.multiplier = 10 ** decimals

    def __str__( self ):
        try:

            return round(math.fabs(self.number), self.decimals).__str__()

        except TypeError as t:
            if isinstance(self.number, list):
                return f"TypeError: {t.__str__()}"

            elif isinstance(self.number, str):
                return f"TypeError: {t.__str__()}"

            elif isinstance(self.number, object):
                return f"TypeError: {t.__str__()}"

        except ValueError as v:
            return f"ValueError: {v.__str__()}"

    def truncate( self ):
        try:

            return int(self.number * self.multiplier) / self.multiplier

        except TypeError as t:
            if isinstance(self.number, list):
                return f"TypeError: {t.__str__()}"

            elif isinstance(self.number, str):
                return f"TypeError: {t.__str__()}"

            elif isinstance(self.number, object):
                return f"TypeError: {t.__str__()}"

        except ValueError as v:
            return f"ValueError: {v.__str__()}"

    def round_up( self ):
        try:

            return math.ceil(self.number * self.multiplier) / self.multiplier

        except TypeError as t:
            if isinstance(self.number, list):
                return f"TypeError: {t.__str__()}"

            elif isinstance(self.number, str):
                return f"TypeError: {t.__str__()}"

            elif isinstance(self.number, object):
                return f"TypeError: {t.__str__()}"

        except ValueError as v:
            return f"ValueError: {v.__str__()}"

    def round_down( self ):
        try:

            return math.floor(self.number * self.multiplier) / self.multiplier

        except TypeError as t:
            if isinstance(self.number, list):
                return f"TypeError: {t.__str__()}"

            elif isinstance(self.number, str):
                return f"TypeError: {t.__str__()}"

            elif isinstance(self.number, object):
                return f"TypeError: {t.__str__()}"

            elif isinstance(self.number, type(self.number)):
                return f"TypeError: {t.__str__()}"

        except ValueError as v:
            return f"ValueError: {v.__str__()}"


if __name__ == '__main__':
    JitRoundNumber()
