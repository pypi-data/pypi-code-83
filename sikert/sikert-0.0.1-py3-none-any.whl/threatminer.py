import requests
from termcolor import colored, cprint

def enum(domain, filename):
    try:
        r=requests.get(f"https://api.threatminer.org/v2/domain.php?q={domain}&rt=5")
        data=r.json()["results"]
        with open(filename, "a") as file:
            for i in range(0, len(data)):
                try:
                    file.writelines("%s\n" % data[i])
                    print(colored("[Threatminer]"+" "+data[i], "blue"))
                except Exception as e:
                    pass
    except Exception as e:
        print("Cannot run source threatminer")