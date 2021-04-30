import requests,time
from .agents import getagent
import concurrent.futures
from .extractdata import extractinfo,cleantag

def load_url(url, pluck):
    resp = requests.get(url,headers=getagent(),timeout=pluck.timeout)
    if pluck.verbose:print(f"Request Status {resp.status_code} :- {url}")
    return resp

def req(csstag,pluck,typ):
  out = {} if pluck.organised else []
  with concurrent.futures.ThreadPoolExecutor(max_workers=pluck.requests) as executor:
    future_to_url = (executor.submit(load_url, url, pluck) for url in pluck.urls)
    time1 = time.time()
    for future in concurrent.futures.as_completed(future_to_url):
        try:
            data = future.result()
            if data.status_code == 200:
             if pluck.organised:out[data.url] = extractinfo(csstag,data,typ)
             else:out.append(extractinfo(csstag,data,typ))
        except Exception as exc:
            if pluck.verbose:print(str(type(exc)))
    time2 = time.time()
  if pluck.verbose:print(f'Took {time2-time1:.2f} s')
  return cleantag(out)