import os
import string

x=raw_input("Enter a number: ")

for i in x :
  if i in string.ascii_lowercase or i in string.ascii_uppercase :
	pass
  elif i in string.digits :
	o=raw_input("Select any option- D to display, E to enter another number, C to clear ")
	if o=='D' :
		print x
		exit
	elif o=='E' :
		y=raw_input("Enter another number: ")
		for j in y :
		 if j in string.ascii_lowercase or j in string.ascii_uppercase :
			pass
		 elif j in string.digits :
			n=raw_input("Select any option - O to perform some operation, C to clear ")
			if n=='C' :
			 pass
			elif n=='O' :
			 y=raw_input("Output")
			 exit
			else :
			 print "Wrong option"
			 exit
		 else :
			print "Wrong input"
	else :
		pass 
  else :
	print "Wrong input"
	exit
