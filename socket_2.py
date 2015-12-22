import urllib.request as ur

mysock = ur.urlopen('http://www.pythonlearn.com/code/intro-short.txt')

op_data = str(mysock.info()) + "\n\n"

for lines in mysock :
  op_data += str(lines)

mysock.close()
f = open('myfile','w')
f.write(op_data)
f.close()
