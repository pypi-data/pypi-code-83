from lxml.cssselect import CSSSelector
from lxml.html import fromstring

def extractinfo(csstag,req):
 sel = CSSSelector(csstag)
 return [e for e in sel(fromstring(req.text))]