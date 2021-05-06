import requests
from termcolor import colored, cprint
def enum(domain, api, filename):
    try:
        headers={'Authorization': 'Bearer %s' % api }
        r=requests.get(f"https://api.certspotter.com/v1/issuances?domain={domain}&include_subdomains=true&expand=dns_names", headers=headers)
        data=r.json()
        with open(filename, "a") as file:
            for i in range(0, len(data)):
                try:
                    for j in range(0, len(data[i]["dns_names"])):
                        try:
                            file.writelines("%s\n" % data[i]["dns_names"][j])
                            print(colored("[Certspotter]"+" "+data[i]["dns_names"][j], "blue"))
                        except Exception as e:
                            pass
                except Exception as e:
                    pass
    except Exception as e:
        print("Cannot run source certspotter")