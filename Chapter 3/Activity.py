"""A program that would accept one(1) integer value not greater than 20,
compute the factorial of the value.

example:
input(1..20): 5
120
"""

from os import system
system("cls")

def factorial(n:int):
	if n==0:
		return 1
	else:
		return n* factorial(n-1)
		
try:
    n:int = int(input("input(1..20):"))
    
    if n>0 and n<=20:
        print(f"The factorial of {n} is {factorial(n)}")
    else:
        print("accept 1 to 20 only")
	

except:
    print("Invalid Input!")