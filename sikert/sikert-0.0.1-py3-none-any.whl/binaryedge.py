import requests
from termcolor import colored

def enum(domain, api, filename):
    try:
        headers={'X-Key': f"{api}"}
        r=requests.get(f"https://api.binaryedge.io/v2/query/domains/subdomain/{domain}", headers=headers)
        data=r.json()["events"]
        with open(filename, "a") as file:
            for i in range(0, len(data)):
                try:
                    file.writelines("%s\n" % data[i])
                    print(colored("[Binary edge]"+" "+data[i]+" ", "blue"))
                except Exception as e:
                    pass
    except Exception as e:
        print("Cannot run source binary edge")