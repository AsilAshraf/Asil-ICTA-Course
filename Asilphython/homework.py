a=['circle','square','triangle']
a[0]='ellipse'
print a
a.insert(0,'rectangle')
print a
a.pop(2)
print a
a.pop(2)
print a

b={1:'circle',2:'square',3:'triangle'}
b['round']=0
print b
print len(b)

del b[2]
print b

