z={1:"hello",2.5:3,"hi":100} #{} for dictionery
print z
print z["hi"] #key value
z[2.5]=9 #mutable value changing directely
print z
print z.keys() #printing all key values
print z.values() #printing all values
print z.items()
for i in z:
	print i,z[i]  #viewing key and value
print z.has_key(1) #for key available or not
print z.get(1) #getting corresponding key value
del z['hi']  #deleting particular key 
print z

	
