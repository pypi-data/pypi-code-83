import requests
from termcolor import colored, cprint

def enum(domain, api, filename):
    try:
        url = "https://api.spyse.com/v3/data/domain/subdomain"
        querystring = {"domain":f"{domain}","limit":"100"}
        headers = {"Accept": "application/json", "Authorization": "Bearer %s" % api}
        r = requests.request("GET", url, headers=headers, params=querystring)
        data=r.json()["data"]["items"]
        with open(filename, "a") as file:
            for i in range(0, len(data)):
                try:
                    file.writelines("%s\n" % data[i]["name"])
                    print(colored("[Spyse]"+" "+data[i]['name'], "blue"))
                except Exception as e:
                    pass
    except Exception as e:
        print("Cannot run source spyse")