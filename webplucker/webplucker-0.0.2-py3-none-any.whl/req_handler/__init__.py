import requests,time
from .agents import getagent
import concurrent.futures
from .extractdata import extractinfo

out = {}

def load_url(url, timeout):
    resp = requests.get(url,headers=getagent(),timeout=timeout)
    print(f"Request Status {resp.status_code} :- {url}")
    return resp

def req(csstag,pluck):
 with concurrent.futures.ThreadPoolExecutor(max_workers=pluck.requests) as executor:
    future_to_url = (executor.submit(load_url, url, pluck.timeout) for url in pluck.urls)
    time1 = time.time()
    for future in concurrent.futures.as_completed(future_to_url):
        try:
            data = future.result()
            if data.status_code == 200:
             out[data.url] = extractinfo(csstag,data)
        except Exception as exc:
            print(str(type(exc)))
    time2 = time.time()
 print(f'Took {time2-time1:.2f} s')
 return out