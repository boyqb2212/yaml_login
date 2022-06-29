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
		mess = input("Enter your message > ")
		mysocket.send(bytes(mess.encode('utf-8')))
		server_message = mysocket.recv(1024)
		yamllogger.logger2.info("[*] Received request : '{}' from server".format(server_message.decode()))

		if mess == "quit":
			yamllogger.logger2.info("END CONNECTION")
			break

except :
	yamllogger.logger2.error("Connect false")
finally:
	mysocket.close()
