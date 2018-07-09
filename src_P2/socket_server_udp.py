import socket

HOST, PORT = "", 12345
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
s.bind((HOST, PORT))


print("Server listening on %s:%s" % (HOST, PORT))

received_packets_count = 0

while(True):
    data, addr = s.recvfrom(1024) # buffer size
    received_packets_count += 1
    print("Received packets: %d" % (received_packets_count))