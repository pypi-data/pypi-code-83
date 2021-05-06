import requests
from termcolor import colored, cprint
def enum(domain, filename):
    try:
        r=requests.get(f"https://sonar.omnisint.io/subdomains/{domain}?page=")
        data=r.json()
        with open(filename, "a") as file:
            for i in range(0, len(data)):
                try:
                    file.writelines("%s\n" % data[i])
                    print(colored("[Project Sonar]"+" "+data[i], "blue"))
                except Exception as e:
                    pass
    except Exception as e:
        print("Cannot run source Project Sonar")