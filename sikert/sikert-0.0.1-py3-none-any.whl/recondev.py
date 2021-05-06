import requests
from termcolor import colored


def enum(domain, api, filename):
    try:
        headers={'Accept' : 'application/json'}
        r=requests.get(f"https://recon.dev/api/search?key={api}&domain={domain}", headers=headers)
        data=r.json()
        with open(filename, "a") as file:
            for i in range(0, len(data)):
                try:
                    for j in range(0, len(data[i]["rawDomains"])):
                        file.writelines("%s\n" % data[i]["rawDomains"][j])
                        print(colored("[Recon Dev]"+" "+data[i]["rawDomains"][j], "blue"))
                except Exception as e:
                    pass
    except Exception as e:
        print("Cannot run source recondev")