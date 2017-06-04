#!/usr/bin/python2

#client_side
import os,getpass,socket

x=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#This is the username of telnet server
username=raw_input("Enter username: ")
#This is the password of telnet server
password=(raw_input("Enter password: "))

x.sendto(username,("192.168.122.1",4321))
x.sendto(password,("192.168.122.1",4321))

print x.recvfrom(100)

while True:
	command=raw_input("Enter command: ")
	x.sendto(command,("192.168.122.1",4321))
	print x.recvfrom(100)[0]
