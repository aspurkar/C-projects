import socket
import json

import sys

MAX_CONNECTIONS = 5  # maximum connection number

with open('config.json') as config_data_file:
    config = json.load(config_data_file)


HOST = config.get('main').get('host')
PORT = config.get('main').get('port')
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create an INET, STREAMing socket
server_socket.bind((HOST, PORT))
server_socket.listen(MAX_CONNECTIONS)  # become a server socket
print

while 1:
    # accept connections from outside
    print >> sys.stderr, 'Waiting for connection at port', PORT
    (connection, address) = server_socket.accept()
    try:
        print 'Connection accepted from ' + repr(address[1])

        while 1:
            data = connection.recv(1024)
            print 'received "%s"' % data
            if data:
                connection.send(json.dumps(config.get(data)))
            else:
                break
    finally:
        connection.close()
