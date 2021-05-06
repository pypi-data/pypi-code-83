import requests
from termcolor import colored, cprint
def enum(domain, filename):
    try:
        r=requests.get(f"https://api.sublist3r.com/search.php?domain={domain}")
        data=r.json()
        with open(filename, "a") as file:
            for i in range(0, len(data)):
                try:
                    file.writelines("%s\n" % data[i])
                    print(colored("[Sublist3r]"+" "+data[i], "blue"))
                except Exception as e:
                    pass
    except Exception as e:
        print("Cannot run source sublist3r")