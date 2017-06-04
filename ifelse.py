x='''Enter 1 if you want to take screenshot
Enter 2 if you want to check date command
Enter 3 if you want to check RAM'''
print x
import os
import commands
y=raw_input()
if y=='1' :
	print "Screenshot message"
	os.system('gnome-screenshot -a')
elif y=='2' :
	print "Date command"
	status,output = commands.getstatusoutput(" date ")
	if status==0 :
	 print output
	else :
	 print "Not Found"
elif y=='3' :
	print "RAM size"
	os.system('dmidecode -t memory | grep -i size')
else :
	print "Wrong input"
