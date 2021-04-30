from webplucker import plucker
db = plucker(['https://free-proxy-list.net/'])
data,output = db.get('#proxylisttable'),[]

def proxylist(px):
  for x in data['https://free-proxy-list.net/']:
    tbody = x.cssselect('tbody tr')
    thead = [xl.text if xl.text!='IP Address' else 'ip' for xl in x.cssselect('thead tr th')]    
    for xx in tbody:output.append(dict(zip(thead, [el.text for el in xx])))
  if px.origin=='all':return output
  else:return [x for x in output if x['Country'].lower()==px.origin.lower()]