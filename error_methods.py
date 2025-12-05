import random

def parity_bit(data, mode="even"):
    bits = ''.join(f"{ord(c):08b}" for c in data)
    ones = bits.count("1")
    if mode == "even":
        return "0" if ones % 2 == 0 else "1"
    return "1" if ones % 2 == 0 else "0"

def parity_2d(data, rows=8, cols=8):
    binary_data = ''.join(f"{ord(c):08b}" for c in data)
    while len(binary_data) < rows * cols:
        binary_data += '0'
    matrix = [binary_data[i*cols:(i+1)*cols] for i in range(rows)]
    row_parity = ''.join(str(sum(int(b) for b in row) % 2) for row in matrix)
    col_parity = ''.join(str(sum(int(matrix[r][c]) for r in range(rows)) % 2) for c in range(cols))
    return row_parity + "|" + col_parity

CRC16_POLY = 0x1021
def crc16(data):
    crc = 0xFFFF
    for ch in data.encode():
        crc ^= ch << 8
        for _ in range(8):
            if crc & 0x8000:
                crc = (crc << 1) ^ CRC16_POLY
            else:
                crc <<= 1
            crc &= 0xFFFF
    return f"{crc:04X}"

def internet_checksum(data):
    total = 0
    byte_data = data.encode()
    if len(byte_data) % 2 == 1:
        byte_data += b'\x00'
    for i in range(0, len(byte_data), 2):
        word = byte_data[i] << 8 | byte_data[i+1]
        total += word
        total = (total & 0xFFFF) + (total >> 16)
    return f"{(~total & 0xFFFF):04X}"
