a=[1,2,"hello",[4,"hi",5.6],3.0]

print a[1]
print a[3]

print a[3][1] #nested string
for i in a:
	print i
a[3][1]="bro"
print a
a[0]=100
print a

a=[1,2,3]
b=a+[1]
#print b

c=b*3
print c
a.append (6)
print a

a=[4,5,6]
b=[7,8,9]
a.extend(b)
print a

a.insert(2,10)
print a

a.pop()
print a

a.pop(3)
print a

#a[::-1]
print a[::-1]
a=[9,8,7]
a.reverse()
print a
