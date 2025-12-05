import socket, random

HOST = "localhost"
PORT = 5000
FORWARD_PORT = 6000

def flip_random_char(data):
    if not data:
        return data
    idx = random.randint(0, len(data)-1)
    return data[:idx] + chr(random.randint(65, 90)) + data[idx+1:]

server = socket.socket()
server.bind((HOST, PORT))
server.listen(1)

print("Server waiting...")

while True:
    conn, addr = server.accept()
    packet = conn.recv(2048).decode()

    data, method, control = packet.split("|")

    corrupted = flip_random_char(data)

    new_packet = f"{corrupted}|{method}|{control}"

    forward = socket.socket()
    forward.connect((HOST, FORWARD_PORT))
    forward.send(new_packet.encode())
    forward.close()

    print("Forwarded:", new_packet)
