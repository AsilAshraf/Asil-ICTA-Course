class person:  #class created
	def __init__(self,name,age,mark):
		self.name = name
		self.age=age
		self.mark=mark
student = person("nikhil",20,9) #object created under the class
print(student.name,student.age,student.mark)
name=raw_input("enter the name")
age=input("enter the age")
mark=input("enter the mark")
student1=person(name,age,mark)
print(student1.name,student1.age,student1.mark)

