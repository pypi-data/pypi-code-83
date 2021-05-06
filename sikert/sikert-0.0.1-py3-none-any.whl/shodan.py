import requests
from termcolor import colored

def enum(domain, api, filename):
    try:
        r=requests.get(f"https://api.shodan.io/dns/domain/{domain}?key={api}")
        data=r.json()["subdomains"]
        with open(filename, "w") as file:
            for i in range(0, len(data)):
                try:
                    file.writelines("%s%s%s\n" % (data[i], ".", f"{domain}") )
                    print(colored("[Shodan]"+" "+data[i]+"."+f"{domain}"+" ", "blue"))
                except Exception as e:
                    pass
    except Exception as e:
        print("Cannot run source shodan")