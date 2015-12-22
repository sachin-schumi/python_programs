import urllib.request as ur
from bs4 import BeautifulSoup
html = ur.urlopen("http://python-data.dr-chuck.net/comments_210621.html").read()

tags = BeautifulSoup(html,'html.parser').findAll('span', attrs={'class':'comments'})
tot_sum = 0.0

for tag in tags :
    tot_sum += float(tag.string)

print (tot_sum)
