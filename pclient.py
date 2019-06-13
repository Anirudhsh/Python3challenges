#!/usr/bin/python
import  socket
recv_ip="127.0.0.1"
recv_port=8787
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
flag=0
while flag==0:
        msg=raw_input("Enter Message")
        if len(msg)>150:
                print("Try Again")
        else:
                s.sendto(msg,(recv_ip,recv_port))
                print(s.recvfrom(150))
                flag=raw_input("Enter 1 to continue And anything else to quit")
                if flag!='1':
                        s.sendto('terminate()',(recv_ip,recv_port))
                        s.close()
                        break
