from webplucker import plucker
db = plucker(['https://free-proxy-list.net/'])
data,output = db.cssselect('#proxylisttable'),[]

def proxylist(px):
  tbody = data.cssselect('tbody tr')
  thead = [xl.text if xl.text!='IP Address' else 'ip' for xl in data.cssselect('thead tr th')]    
  for xx in tbody:output.append(dict(zip(thead, [el.text for el in xx])))
  if px.origin=='all':return output
  else:return [x for x in output if x['Country'].lower()==px.origin.lower()]