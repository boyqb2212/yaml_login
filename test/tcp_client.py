#!/usr/bin/python
 
import socket
import yamllogger

host="127.0.0.1"
port = 9993

try:
	mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	mysocket.connect((host, port))
	yamllogger.logger2.info('Connected to host '+str(host)+' in port: '+str(port))
	message = mysocket.recv(1024)
	print("Message received from the server", message)
	while True:
		message = input("Enter your message > ")
		mysocket.send(bytes(message.encode('utf-8')))
		if message== "quit":
			yamllogger.logger2.info("END CONNECTION")
			break
		if message== "chui bay":
			yamllogger.logger2.warning("FPI WARNING")

		if message== "noi tuc":
			yamllogger.logger2.warning("FPI WARNING")

except :
	yamllogger.logger2.error("Can't connect ")
finally:
	mysocket.close()
