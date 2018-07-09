import socket

HOST, PORT = "140.112.42.108", 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP
s.connect((HOST, PORT))

print("connected to " + HOST)

while(True):
	message = s.recv(1000).decode('utf-8')

	if not message:
		break

	print("Receive server message:")

	if "(Session End)" in message or "Please retry it again." in message:
		print(message)
		break

	response = input(message)
	s.send(bytes(response, 'utf-8'))

s.close()