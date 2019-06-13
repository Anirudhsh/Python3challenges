#!/usr/bin/python
import socket
recv_ip="127.0.0.1"
recv_port=8787
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((recv_ip,recv_port))
while True:
        data=s.recvfrom(150)
        if data[0]=='terminate()':
                print("connection terminated")
                s.close()
                break
        else:
                print("Message_from sender::",data[0])
                print("sender IP + socket::",data[1])
                msg=raw_input("Enter Message")
        if len(msg) > 150:
                print("reply in 150 characters")
        else:
                        s.sendto(msg,data[1])
