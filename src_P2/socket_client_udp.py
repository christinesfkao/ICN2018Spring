import socket

PACKETS_AMOUNT = 10000

HOST, PORT = "", 12345
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

print("Sending %d packets to %s:%s" % (PACKETS_AMOUNT, HOST, PORT))

for x in range(0, PACKETS_AMOUNT):
	s.sendto(b"ping", (HOST, PORT))