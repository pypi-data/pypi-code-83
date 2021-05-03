import numpy as np
from functools import reduce



class StatsLog:
    def __init__(self, funcs:list, spaces="  ", viznt_funcs=[], path=None):
        """
        Arguments:
        :funcs = <list>
            List of functions for statistical information.
        :spaces = <str>
            Margins in a row, between columns of statistical information that the write function returns.
        :non_viz_funcs = <list>
            Contains a list of functions whose results are recorded in log, but not displayed on the screen.
        :path = <str>
            Path for writing statistical information to a csv or json file.
        """
        self.funcs = funcs
        self.viznt_funcs = viznt_funcs
        self.spaces = spaces
        self.__path = path
        if self.__path != None:
            self.__doc = open(self.__path, "w")
        self.headers = self.__create_headers()
        self.log = {}
        self.__gen = 0


    def write(self, pop) -> str:
        """
        Calculating and storing statistical information.
        Arguments:
        :pop = <Population>
            Return
        :<str>
            A string of statistical information.
        """


        self.__gen += 1
        self.log[self.__gen] = {}
        #calculate value of funcs
        for func in self.funcs + self.viznt_funcs:
            self.log[self.__gen][f"{func.__name__}"] = func( pop )

        #create string for return
        ret_str = f"{self.__gen}"+"|"+self.spaces
        for key in self.log[self.__gen]:
            if key not in [ func.__name__ for func in self.viznt_funcs ]:
                ret_str += str(self.log[self.__gen][key])+"|"+self.spaces
        
        #write string to doc
        self.__write_doc(string=ret_str)
        return ret_str

    def __write_doc(self, string):
        self.__doc.write(string+"\n")
        
    def __create_headers(self):
        str_headers = "gen" + "|" + self.spaces
        for func in self.funcs:
            if func.__name__ not in [ func.__name__ for func in self.viznt_funcs ]:
                str_headers += func.__name__ + "|" + self.spaces
        self.__doc.write(str_headers+"\n")
        return str_headers