f=open("test.dat","w")
f.write("1234")
f.write("slcse")
f.close()
f=open("test.dat","r")
print (f.read())
f.close()