'''
# Fibonacci Sequence Generator
# Have the user enter a number and
# generate a fibonacci sequence
# which size is equivalent to that number.
https://github.com/SubhamSubhasisPatra/Fibonacci-Sequence-
'''
n = int(input("Enter the number : "))

def fibon(n):
	new_list = []
	a=0
	b=1
	for x in range(n):
		 a,b = b,a+b
		 new_list.append(a)
	return new_list
	
print(list(fibon(n)))