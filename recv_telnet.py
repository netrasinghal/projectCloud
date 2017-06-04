#!/usr/bin/python2

#server_side
import getpass,os,socket,commands

x=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
x.bind(("",4321))

data=x.recvfrom(100)
data1=x.recvfrom(100)
if data[0]=='root' and data1[0]=='redhat' :
	x.sendto("CONNECTED",data[1])
	while True:
		command=x.recvfrom(100)[0]
		output=commands.getoutput(command)
		x.sendto(output,data[1])

else :
	x.sendto("NOT CONNECTED",data1[1])
