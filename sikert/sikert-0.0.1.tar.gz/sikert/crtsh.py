import requests
from termcolor import colored, cprint

def enum(domain, filename):
    try:
        r=requests.get(f"https://crt.sh/?q={domain}&output=json")
        data=r.json()
        with open(filename, "a") as file:
            for i in range(0, len(data)):
                try:
                    file.writelines("%s\n" % data[i]["common_name"])
                    print(colored("[Certsh]"+" "+data[i]["common_name"], "blue"))
                except Exception as e:
                    pass
    except Exception as e:
        print("Cannot run source certsh")