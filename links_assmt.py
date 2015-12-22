import urllib.request as ur
from bs4 import BeautifulSoup

url = "https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Isimeli.html"
url_text = ""

for i in range(0,7) :
  count = 0
  html = ur.urlopen(url).read()
  soup = BeautifulSoup(html,'html.parser')
  tags = soup('a')
  for tag in tags :
    url = tag.get('href',None)
    url_text = tag.string
    count = count + 1
    if count == 18 :
      break

print(url_text)
