import socket
from error_methods import parity_bit, parity_2d, crc16, internet_checksum

methods = {
    "PARITY": parity_bit,
    "2DPARITY": parity_2d,
    "CRC16": crc16,
    "CHECKSUM": internet_checksum
}

HOST = "localhost"
PORT = 5000

sock = socket.socket()
sock.connect((HOST, PORT))

data = input("Enter text: ")
print("Methods: PARITY, 2DPARITY, CRC16, CHECKSUM")
method = input("Select method: ").upper()

control = methods[method](data)

packet = f"{data}|{method}|{control}"
sock.send(packet.encode())

print("Packet sent:", packet)
sock.close()
