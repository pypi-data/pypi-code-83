import requests
from termcolor import colored


def enum(domain, api, filename):
    try:
        url = 'https://www.virustotal.com/vtapi/v2/domain/report'
        params = {'apikey':f'{api}', 'domain': f'{domain}'}
        r = requests.get(url, params=params)
        data=r.json()["subdomains"]
        with open(filename, "a") as file:
            for i in range(0, len(data)):
                try:
                    file.writelines("%s\n" % data[i])
                    print(colored("[Virus Total]"+" "+data[i], "blue"))
                except Exception as e:
                    pass
    except Exception as e:
        print("Cannot run source virus total")