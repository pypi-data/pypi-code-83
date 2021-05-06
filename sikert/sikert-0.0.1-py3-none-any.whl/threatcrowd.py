
import requests
from termcolor import colored, cprint

def enum(domain, filename):
    try:
        r=requests.get(f"https://www.threatcrowd.org/searchApi/v2/domain/report/?domain={domain}")
        data=r.json()["subdomains"]
        with open(filename, "a") as file:
            for i in range(0, len(data)):
                try:
                    file.writelines("%s\n" % data[i])
                    print(colored("[Threatcrowd]"+" "+data[i], "blue"))
                except Exception as e:
                    pass
    except Exception as e:
        print("Cannot run source threatcrowd")