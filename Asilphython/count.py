#str="this is string example of aeiou wow....";
#print str.count("i",4,40)
#print "wow occur in",str.count("wow")

s=raw_input("enter the string")
n=0
p=0
k=0
c=0
for i in s:
	if i in "aeiouAEIOU":
		n=n+1
	elif i in s:
		p=p+1
	elif i in " ":
		k=k+1
for i in s:
	if i in "?":
		c=c+1

print ("number of vowels is",n)
print ("the number of constants is",p)
print ("the number of words are",k+1)
print ("the number of ? is",c)
