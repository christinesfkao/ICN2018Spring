from socket import *
import sys

HOST, PORT = "", 8080 # HTTP on MacOS, replacement for 80

# Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)
# Fill in start.
# tcpSersock.connect((HOST, PORT))
tcpSerSock.bind((HOST, PORT))
tcpSerSock.listen(0)

# Fill in end.
while 1:
	# Start receiving data from the client
	print('Ready to serve...')
	tcpCliSock, addr = tcpSerSock.accept()
	print('Received a connection from:', addr)
	# Fill in start.	
	message = tcpCliSock.recv(1000).decode('utf-8')
	if not message: # debug
		continue
	# Fill in end.
	print(message)
	# Extract the filename from the given message
	print(message.split()[1])
	filename = message.split()[1].partition("/")[2]
	print(filename)
	fileExist = "false"
	filetouse = "/" + filename
	print(filetouse)
	try:
		# Check whether the file exists
		f = open(filetouse[1:], "r")
		outputdata = f.read() # instead of readlines()
		fileExist = "true"
		# WebServer finds file and generates a response message
		tcpCliSock.send(b"HTTP/1.0 200 OK\r\n")
		tcpCliSock.send(b"Content-Type:text/html\r\n")
		# Fill in start.
		tcpCliSock.send(b"\r\n") # return empty line due to HTTP protocol spec
		tcpCliSock.send(bytes(outputdata, 'utf-8'))
		tcpCliSock.send(b"\r\n") # return empty line due to HTTP protocol spec
		# Fill in end.
		print('Read from file')
	# Error handling for file not found
	except IOError:
		# Fill in start.
		print("File not found.")
		tcpCliSock.send(b"HTTP/1.0 404 Not Found\r\n")
		tcpCliSock.send(b"Content-Type:text/html\r\n")		
		tcpCliSock.send(b"\r\n") # return empty line due to HTTP protocol spec
		tcpCliSock.send(b"<!DOCTYPE html><html><head><meta charset=\"UTF-8\"><title>404 Not Found</title></head><body><h1>404 Not Found</h1></body></html>")
		tcpCliSock.send(b"\r\n") # return empty line due to HTTP protocol spec
		# Fill in end.
		tcpCliSock.send
	# Close the client and the server sockets
	tcpCliSock.close()
# Fill in start.
# Fill in end.
