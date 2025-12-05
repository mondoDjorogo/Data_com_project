# Socket Programming – Error Detection

This project simulates data transmission using Python sockets.  
Client 1 sends a message with generated error-detection bits (Parity, 2D Parity, CRC16, or Checksum).  
The Server receives the packet, applies random data corruption, and forwards it.  
Client 2 receives the corrupted packet, recalculates the control bits, and checks if the data is correct or corrupted.

Run order:  
1) client2_receiver.py  
2) server_corruptor.py  
3) client1_sender.py  

Wireshark can be used to observe packets between clients and the server.
