#! /usr/bin/python3
import requests,argparse,sys,colorama,pyfiglet
from colorama import Fore,Style

class Covid:
    colorama.init(autoreset=True)
    parser = argparse.ArgumentParser(description="View By Country")
    parser.add_argument("country",nargs="?",metavar="",type=str,help="radius")
    parser.add_argument("-d","--deaths",action="store_true",help="deaths")
    parser.add_argument("-c","--cases",action="store_true",help="total cases")
    parser.add_argument("-g","--todayCases",action="store_true",help="today cases")
    parser.add_argument("-f","--deathsToday",action="store_true",help="deaths")
    parser.add_argument("-r","--recovered",action="store_true",help="recovered")
    parser.add_argument("-e","--todayRecovered",action="store_true",help="todayRecovered")
    parser.add_argument("-b","--critical",action="store_true",help="critical")
    parser.add_argument("-a","--active",action="store_true",help="active")
    parser.add_argument("-i","--tests",action="store_true",help="tests")
    parser.add_argument("-t","--today",action="store_true",help="today's cases")
    args  = parser.parse_args()
    base_url = "https://disease.sh/v3/covid-19/"
    def _myLocation(self):
        response = requests.get("https://freegeoip.app/json/")
        if response.status_code == 200:
            country = response.json().get('country_name')
            return country
    def _getResponse(self,endpoint):
        response = requests.get(endpoint)
        if response.status_code == 200:
            return response.json()
    @staticmethod
    def printOut(arg,value):
        if arg != "country":
            sys.stdout.write(f"{Fore.RED}[+] {Fore.BLUE}{Style.BRIGHT}{arg}: {Fore.WHITE}{Style.BRIGHT}{int(value):,} \n")
        else:
            sys.stdout.write(f"{Fore.RED}[+] {Fore.BLUE}{Style.BRIGHT}{arg}: {Fore.WHITE}{Style.BRIGHT}{value} \n")
        sys.stdout.flush()
    @property
    def stats(self):
        mycountry = self.args.country if self.args.country else self._myLocation()
        if mycountry:
            args_status = False
            json_response = self._getResponse(f"{self.base_url}countries/{mycountry}")
            sys.stdout.write(pyfiglet.figlet_format("Covid Tracker",justify="center"))
            sys.stdout.flush()
            if json_response:
                if self.args.cases:
                    self.printOut("cases",json_response.get("cases"))
                    args_status = True
                if self.args.deaths:
                    self.printOut("deaths",json_response.get("deaths"))
                    args_status = True
                if self.args.recovered:
                    self.printOut("recovered",json_response.get("recovered"))
                    args_status = True
                if self.args.critical:
                    self.printOut("critical",json_response.get("deaths"))
                    args_status = True
                if self.args.active:
                    self.printOut("active",json_response.get("active"))
                    args_status = True
                if self.args.tests:
                    self.printOut("tests",json_response.get("tests"))
                    args_status = True
                if self.args.today:
                    self.printOut("todayCases",json_response.get("todayCases"))
                    self.printOut("todayRecovered",json_response.get("todayRecovered"))
                    self.printOut("deathsToday",json_response.get("todayDeaths"))
                    args_status = True
                else:              
                    if self.args.todayCases:
                        self.printOut("todayCases",json_response.get("todayCases"))
                        args_status = True
                    if self.args.deathsToday:
                        self.printOut("deathsToday",json_response.get("todayDeaths"))
                        args_status = True
                    if self.args.todayRecovered:
                        self.printOut("todayRecovered",json_response.get("todayRecovered"))
                        args_status = True
                if not args_status:
                    exclude = ("updated","countryInfo","undefined","continent")
                    for key in exclude:
                        json_response.pop(key)
                    for key in json_response:
                        self.printOut(key,json_response[key])
        else:
            sys.exit("something went wrong")
if __name__ == "__main__":
    Covid().stats