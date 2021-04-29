from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError, InvalidTZPathWarning


class JitTimes:

    def __init__( self,
                  TS: float = '',  # datetime.now().timestamp(),
                  dt_format: str = '%Y-%m-%d %H:%M:%S',
                  tz_info: str = '' ):
        """
        self.TS # Time stamp
        self.dt_format # format datetime
        self.tz_info # zone info
        """
        self.TS = TS
        self.dt_format = dt_format
        self.tz_info = tz_info

    def __str__( self ):
        try:
            if self.tz_info != '':
                return self.tzInfo().strftime(self.dt_format)
            else:
                return self.get_convert_datetime().strftime(self.dt_format)
        except TypeError as t:
            return t.__str__()
            # return "Error time stamp {}".format(t.__str__())
        except AttributeError as a:
            return a.__str__()

    """ Private Function
        Using convert `time stamp` to `datetime` 
    """

    def get_convert_datetime( self ) -> object:

        return datetime.fromtimestamp(self.TS)

    @staticmethod
    def convert_timestamp( dt: str ):
        return datetime.fromisoformat(dt).timestamp()

    def tzInfo( self ):
        try:
            tzInfo = ZoneInfo(self.tz_info)
            return self.get_convert_datetime().astimezone(tz=tzInfo)

        except TypeError as te:
            return { 'error_message': te.__str__(), 'dt_time': self.__str__() }

        except ValueError as v:
            return "ValueError :>_ " + v.__str__()

        except ZoneInfoNotFoundError as ze:
            return "ZoneInfoNotFoundError :>_ " + ze.__str__()

        except InvalidTZPathWarning as izpw:
            return "InvalidTZPathWarning :_> " + izpw.__str__()
        except RecursionError as re:
            return re.__str__()

    """ พุทธศักราช """

    def buddhistEra( self ):
        cdt = self.get_convert_datetime()
        year = datetime.date(cdt).year + 543
        date = datetime.date(cdt).replace(year=year)
        time = datetime.time(cdt)

        self.TS = self.convert_timestamp("{} {}".format(date, time))
        return self.__str__()

    """ ฮิจเราะห์ศักราช """

    def hijriEra( self ):
        cdt = self.get_convert_datetime()
        year = (datetime.date(cdt).year + 543) - 1164

        date = datetime.date(cdt).replace(year=year)
        time = datetime.time(cdt)

        self.TS = self.convert_timestamp("{} {}".format(date, time))
        return self.__str__()
