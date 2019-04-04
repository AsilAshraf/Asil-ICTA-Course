def factorial(n):
	if n==0:  
		return 1  #change n=0 into 1 for corect answer
	else:
		return n*factorial(n-1)  #recursion-function calling inside its function
n=int(input("enter no"))
print factorial(n)

