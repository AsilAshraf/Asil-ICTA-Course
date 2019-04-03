a=[]
num=int(input("howmany numbers for adding:"))
for n in range(num):
	numbers=int(input("enter numbers:"))
	a.append(numbers)
print a
print "maximum number is:",max(a)
print "minimum number is:",min(a)
