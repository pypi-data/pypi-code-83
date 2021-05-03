from pprint import pprint

from persiantools.jdatetime import JalaliDate
from persiantools import characters, digits
from datetime import datetime
import re


"""This Is StringC class which is inherit from str class"""


class StringC(str):
    """This class Inherit from str Class
        Attributes:
            Any string

        Examples:
            string = StringC("تاریخ برعکس  ۱۳۹۹-۱۱-۳۰ تاریخ میلادی 1999/03/02 و تاریخ میلادی برعکس 05/12/95 حروف عربی مثل كيك  ۱۳۹۹/۱۱/۳۰  تاریخ")
            string.convert
            Output:
            "تاریخ برعکس  1399-11-30 تاریخ میلادی 1999/03/02 و تاریخ میلادی برعکس 05/12/95 حروف عربی مثل کیک  1399/11/30  تاریخ"
    """
    def __init__(self, content):
        """
        -Any Number in string will convert to En string Number

        -Any Arabic Character in string will convert to Farsi
        """
        super().__init__()
        self.convert = digits.fa_to_en(characters.ar_to_fa(digits.ar_to_fa(content)))

    @staticmethod
    def dates(content):
        """
        :param content: str
        :return: list of datetime object
        At the beginning :
            -Any Number in string will convert to En string Number
            -Any Arabic Character in string will convert to Farsi

        For now it just find dates in numeric formats which are separated with characters like "-" or "/" or "."
        There is no difference if date is Jalali or Gregorian or Characters are Fa or Ar,
         this function convert date to Gregorian datetime object

        Examples:
            from StringC import StringC


            string = "Today is 1400/01/18"
            type(StringC.dates(string))
            type(StringC.dates(string)[0])
            StringC.dates(string)
            Output:
            <class 'list'>
            <class 'datetime.datetime'>
            [datetime.datetime(2021, 4, 7, 0, 0)]

            string = "today is 2021/04/05"
            Output:
            [datetime.datetime(2021, 4, 5, 0, 0)]

            string = "today is 2021/04/07 and Today is 1400/01/18 yesterday was 17/01/1400 yesterday also was 06/04/2021"
            Output:
            [
                datetime.datetime(2021, 4, 7, 0, 0),
                datetime.datetime(2021, 4, 7, 0, 0),
                datetime.datetime(2021, 4, 6, 0, 0),
                datetime.datetime(2021, 4, 6, 0, 0)
            ]


        """
        content = digits.fa_to_en(characters.ar_to_fa(digits.ar_to_fa(content)))
        # Find Date in string by re pattern:
        datesTemp = re.findall("(\d+)[-/.](\d+)[-/.](\d+)", content)
        dates = list()
        # Convert date from string to integer:
        for date in range(len(datesTemp)):
            datesTemp[date] = list(datesTemp[date])
            for num in range(len(datesTemp[date])):
                datesTemp[date][num] = int(datesTemp[date][num])

        # Convert dates To gregorian Date Object
        for date in datesTemp:
            try:
                temp = JalaliDate(*date).to_gregorian()
                temp = datetime.combine(temp, datetime.min.time())
                if temp.year > 2100 or temp.year < 1300:
                     temp = datetime(*date)
            except ValueError:
                date.reverse()
                # print(date)
                try:
                    temp = JalaliDate(*date).to_gregorian()
                    temp = datetime.combine(temp, datetime.min.time())
                    if temp.year > 2100 or temp.year < 1300:
                        temp = datetime(*date)
                except ValueError:
                    temp = None
                except Exception as e:
                    temp = None
                    pprint(e)
            if temp:
                dates.append(temp)

        return dates

    def __repr__(self):
        """
        :return: Converted String:
                -Any Number in string will convert to En string Number
                -Any Arabic Character in string will convert to Farsi
        """
        return self.convert


