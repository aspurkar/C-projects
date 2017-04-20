import socket
import json
import re

with open('config.json') as config_data_file:
    config = json.load(config_data_file)

HOST, PORT = config.get('main').get('host'), config.get('main').get('port')
MODE, FIRST_NUMBER, SECOND_NUMBER = '', 0, 0

print 'Welcome to fake dns application'
print 'You can enter expression like 5+4 or 4/3 to get calculation back or enter "help" for help'
while True:
    try:
        input_data = raw_input("Please enter expression or type 'help': \n")
        if input_data.lower() == 'help':
            print 'Not an error: No help, survive. Muahahaha'
            continue

        exp = re.split("([+-/*])", input_data.strip().replace(" ", ""))
        FIRST_NUMBER = int(exp[0])
        SECOND_NUMBER = int(exp[2])
        mode = ''
        if exp[1] == '+':
            MODE = 'addition'
        elif exp[1] == '-':
            MODE = 'subtraction'
        elif exp[1] == '*':
            MODE = 'multiplication'
        elif exp[1] == '/':
            MODE = 'division'
        else:
            raise Exception('Error: Yo dude. I need an expression')
        break
    except ValueError:
        print "Error: Dude. Enter numbers"
        continue
    except Exception as err:
        print err
        continue

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.settimeout(1000)

# connecting to dns server
client_socket.connect((HOST, PORT))

try:
    print 'Connected to dns server at', HOST, 'and port number', PORT
    client_socket.send(MODE)
    response = client_socket.recv(1024)
    print 'Received a response from dns server...'
    print 'Response:', response
finally:
    client_socket.close()

print
print
if not response:
    print 'Wrong response. Shutting down'
    quit()

response = json.loads(response)

if 'port' and 'host' not in response.keys():
    print 'Wrong response. Shutting down'
    quit()

# connection to operation server
print
print

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.settimeout(1000)
client_socket.connect((response.get('host'), response.get('port')))
try:
    print 'Connected to ', MODE, 'server at', response.get('host'), 'and port', response.get('port')
    obj = {'a': FIRST_NUMBER, 'b': SECOND_NUMBER}
    message = json.dumps(obj)
    client_socket.send(message)
    data = client_socket.recv(1024)
    data = json.loads(data)
    print "Operation result is ", data.get('result')
finally:
    client_socket.close()
