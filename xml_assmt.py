import xml.etree.ElementTree as ET
import urllib.request as ur

url = "http://python-data.dr-chuck.net/comments_210618.xml"
xml_data = ur.urlopen(url).read()

tree = ET.fromstring(xml_data)
op_sum = 0

op_list = tree.findall('comments/comment')

for op in op_list:
  op_sum+= int(op.find('count').text)

print(op_sum)

