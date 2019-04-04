def sum(a,b):
	return a+b
def sub(a,b):
	return a-b
def mul(a,b):
	return a*b
def div(a,b):
	if b==0:  
		print "enter a number not zero"
	else:
		return a/b
print "1.add\n2.sub\n3.mul\n.4.div"
choice=int(input("enter ur choice"))
a=int(input("enter ur 1st number"))
b=int(input("enter ur 2nd number"))
if choice==1:
	print sum(a,b)
elif choice==2:
	print sub(a,b)
elif choice==3:
	print mul(a,b)
elif choice==4:
	print div(a,b)
else:
	print"invalid choice"


