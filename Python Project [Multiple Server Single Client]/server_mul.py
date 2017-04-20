import socket
import json

import sys

MAX_CONNECTIONS = 5  # maximum connection number

with open('config.json') as config_data_file:
    config = json.load(config_data_file)

HOST = config.get('multiplication').get('host')
PORT = config.get('multiplication').get('port')


def addition(a, b):
    return a + b


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create an INET, STREAMing socket
sock.bind((HOST, PORT))
sock.listen(MAX_CONNECTIONS)  # become a server socket
print

while 1:
    # accept connections from outside
    print >> sys.stderr, 'Waiting for connection on port', PORT
    (connection, address) = sock.accept()
    try:
        print 'Connection accepted from ' + repr(address[1])

        while 1:
            data = connection.recv(1024)
            print 'received "%s"' % data
            if data:
                try:
                    data = json.loads(data)
                except:
                    print 'Cannot decode json'
                    connection.send('error')
                    break

                if 'a' in data.keys() and 'b' in data.keys():
                    res = json.dumps({'result' : int(data.get('a')) * int(data.get('b'))})
                    connection.send(res)
                    print 'Sending', res, 'response to client'
                else:
                    break
            else:
                break
    finally:
        print 'Shutting down the connection with', repr(address[1])
        connection.close()
