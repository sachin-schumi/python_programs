import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
mysock.send(("GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n").encode('utf-8'))

op_data = ""

while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    op_data += str(data)

mysock.close()
f = open('myfile','w')
f.write(op_data)
f.close()
