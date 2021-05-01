import datetime, urllib.request, json

def getResponse(url):
  '''Given a URL, returns json data from it
  '''
  operUrl = urllib.request.urlopen(url)
  if(operUrl.getcode() == 200):
    data = operUrl.read()
    jsonData = json.loads(data)
  else:
    print("Error receiving data", operUrl.getcode())
  return jsonData

class Nyse:
  '''New York Stock Exchange'''
  def trading_day(d,e=0):
    '''trading_day(d,e=0) -> bool
  
       d is a datetime date, e is an int representing a year
  
       Returns True if d is a NYSE trading day, and false otherwise.
       Omit e or set it to 0 if dealing with actual dates; for expected
       dates, set e to the year from which you are projecting.
       Use dates after 1 January 1971! The function may be inaccurate
       with earlier dates.
    '''
    url = "https://dl29henb28.execute-api.us-east-1.amazonaws.com/test/datetime-requests?func=nysetd&"
    url += "dy={dy}&dm={dm}&dd={dd}&e={e}".format(dy = d.year, dm = d.month, dd = d.day, e = e)
    return getResponse(url)['ret']
  
  def td(d,e=0):
    '''td(d,e=0) -> bool
  
       d is a datetime date, e is an int representing a year  
  
       Returns True if d is a NYSE trading day, and false otherwise.
       Omit e or set it to 0 if dealing with actual dates; for expected
       dates, set e to the year from which you are projecting.
       Use dates after 1 January 1971! The function may be inaccurate
       with earlier dates.
    '''
    url = "https://dl29henb28.execute-api.us-east-1.amazonaws.com/test/datetime-requests?func=nysetd&"
    url += "dy={dy}&dm={dm}&dd={dd}&e={e}".format(dy = d.year, dm = d.month, dd = d.day, e = e)
    return getResponse(url)['ret']

  def holiday(d,e=0):
    '''holiday(d,e=0) -> bool

       d is a datetime date

       Returns True if d is a NYSE holiday, and false otherwise.
       Omit e or set it to 0 if dealing with actual dates; for expected
       dates, set e to the year from which you are projecting.
       Use dates after 1 January 1971! The function may be inaccurate
       with earlier dates.

       (Note that if a holiday falls on a weekend, its actual observance 
       may fall on a different date!)
    '''
    if(e == 0):
      e = d.year
    url = "https://dl29henb28.execute-api.us-east-1.amazonaws.com/test/datetime-requests?func=nyseholiday&"
    url += "dy={dy}&dm={dm}&dd={dd}&e={e}".format(dy = d.year, dm = d.month, dd = d.day, e = e)
    return getResponse(url)['ret']

  def days_between_actual(a,b):
    '''days_between_actual(a,b) -> int
  
       a and b are both datetime dates
       
       Returns the number of actual NYSE trading days between a and b.
    '''
    url = "https://dl29henb28.execute-api.us-east-1.amazonaws.com/test/datetime-requests?func=nysedba&"
    url += "ay={ay}&am={am}&ad={ad}&".format(ay = a.year, am = a.month, ad = a.day)
    url += "by={by}&bm={bm}&bd={bd}".format(by = b.year, bm = b.month, bd = b.day)
    return getResponse(url)['ret']

  def dba(a,b):
    '''dba(a,b) -> int
  
       a and b are both datetime dates
  
       Returns the number of actual NYSE trading days between a and b.
    '''
    url = "https://dl29henb28.execute-api.us-east-1.amazonaws.com/test/datetime-requests?func=nysedba&"
    url += "ay={ay}&am={am}&ad={ad}&".format(ay = a.year, am = a.month, ad = a.day)
    url += "by={by}&bm={bm}&bd={bd}".format(by = b.year, bm = b.month, bd = b.day)
    return getResponse(url)['ret']

  def days_between_expected(a,b):
    '''days_between_expected(a,b) -> int

       a and b are both datetime dates
  
       Returns the number of expected NYSE trading days between a and b.
       Projects from a's year, assuming that a's calendar schedule will continue forever
    '''
    url = "https://dl29henb28.execute-api.us-east-1.amazonaws.com/test/datetime-requests?func=nysedbe&"
    url += "ay={ay}&am={am}&ad={ad}&".format(ay = a.year, am = a.month, ad = a.day)
    url += "by={by}&bm={bm}&bd={bd}".format(by = b.year, bm = b.month, bd = b.day)
    return getResponse(url)['ret']

  def dbe(a,b):
    '''dbe(a,b) -> int
  
       a and b are both datetime dates
  
       Returns the number of expected NYSE trading days between a and b.
       Projects from a's year, assuming that a's calendar schedule will continue forever
    '''
    url = "https://dl29henb28.execute-api.us-east-1.amazonaws.com/test/datetime-requests?func=nysedbe&"
    url += "ay={ay}&am={am}&ad={ad}&".format(ay = a.year, am = a.month, ad = a.day)
    url += "by={by}&bm={bm}&bd={bd}".format(by = b.year, bm = b.month, bd = b.day)
    return getResponse(url)['ret']


