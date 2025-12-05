import socket
from error_methods import parity_bit, parity_2d, crc16, internet_checksum

methods = {
    "PARITY": parity_bit,
    "2DPARITY": parity_2d,
    "CRC16": crc16,
    "CHECKSUM": internet_checksum
}

HOST = "localhost"
PORT = 6000

server = socket.socket()
server.bind((HOST, PORT))
server.listen(1)

print("Client 2 ready...")

while True:
    conn, addr = server.accept()
    packet = conn.recv(2048).decode()

    data, method, incoming_control = packet.split("|")

    computed = methods[method](data)

    print("\n===== RESULT =====")
    print("Received Data:", data)
    print("Method:", method)
    print("Sent Check Bits:", incoming_control)
    print("Computed Check Bits:", computed)
    print("Status:", "DATA CORRECT" if computed == incoming_control else "DATA CORRUPTED")
    print("==================\n")
