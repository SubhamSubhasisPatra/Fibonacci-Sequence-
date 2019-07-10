'''
# Fibonacci Sequence Generator
# Have the user enter a number and
# generate a fibonacci sequence
# which size is equivalent to that number.
https://github.com/SubhamSubhasisPatra/Fibonacci-Sequence-
'''
n = int(input("Enter the number : "))

def fibon(n):
	a=1
	b=1
	for x in range(n):
		 yield a
		 a,b = b,a+b
	
print(list(fibon(n)))