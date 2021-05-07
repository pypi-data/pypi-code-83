import URLs # importon file me json qe permban keys dhe URLS per webscraping si value
from URLs import data




import requests
from bs4 import BeautifulSoup
from functools import lru_cache

response = []

@lru_cache(maxsize = 100)
def WebScrape(URL):
    r = requests.get(URL, headers = {'User-agent': 'Super Bot Power Level Over 9000'})
    response.append(r.status_code)
    result = BeautifulSoup(r.content, "html.parser").find("div", attrs = {"class":"BNeawe tAd8D AP7Wnd"})
    return result.text


for r, ref in enumerate(data):

    try:
        result = "{}/{}".format(ref, WebScrape(data[ref]).split("\n")[1])
    except:
        result = "{}/ERROR!{}".format(ref, str(response))

    if response == str([429]):
        print(response)
        break

    with open("sample.txt", "a") as file:
        file.write('\n'+ result)


    response = []

    print(r, result)



