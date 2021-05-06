import requests
from termcolor import colored


def enum(domain, api, filename):
    try:
        url = f"https://api.securitytrails.com/v1/domain/{domain}/subdomains"
        querystring = {"children_only":"false"}
        headers = {"Accept": "application/json","APIKEY": f"{api}"}
        r = requests.get(url, headers=headers, params=querystring)
        data = r.json()["subdomains"]
        with open(filename, "a") as file:
            for i in range(0, len(data)):
                try:
                    file.writelines("%s\n" % data[i])
                    print(colored("[Security Trails]"+" "+data[i]+"."+f"{domain}", "blue"))
                except Exception as e:
                    pass
    except Exception as e:
        print("Cannot run source security trails")