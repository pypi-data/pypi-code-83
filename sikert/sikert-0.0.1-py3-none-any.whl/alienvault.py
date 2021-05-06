import requests
from termcolor import colored
def enum(domain, filename):
    try:
        r=requests.get(f"https://otx.alienvault.com/api/v1/indicators/domain/{domain}/passive_dns")
        data=r.json()["passive_dns"]
        with open(filename, "a") as file:
            for i in range(0, len(data)):
                try:
                    file.writelines("%s\n" % data[i]["hostname"])
                    print(colored("[Alien Vault]"+" "+data[i]["hostname"], "blue"))
                except Exception as e:
                    pass
    except Exception as e:
        print("Cannot run source alien vault")