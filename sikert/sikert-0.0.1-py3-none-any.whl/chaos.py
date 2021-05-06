import requests
from termcolor import colored

def enum(domain, api, filename):
    try:
        headers={"Authorization" : f"{api}"}
        r=requests.get(f"https://dns.projectdiscovery.io/dns/{domain}/subdomains", headers=headers)
        data=r.json()["subdomains"]
        with open(filename, "a") as file:
            for i in range(0, len(data)):
                try:
                    file.writelines("%s%s%s\n" % (data[i], ".", f"{domain}"))
                    print(colored("[Chaos]"+" "+data[i]+"."+f"{domain}", "blue"))
                except Exception as e:
                    pass
    except Exception as e:
        print("Cannot run source chaos")
