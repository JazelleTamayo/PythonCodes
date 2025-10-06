
from os import system
from arithmetic import add
from constants import pi
#import arithmetic
import constants
#import objects
system('cls')

def main():
    num1: int = int(input("Enter number: "))
    num2: int = int(input("Enter another number: "))
    print(add(num1, num2))
    # Call the add function directly from the arithmetic module
    #print(arithmetic.add(num1, num2))
    #print(arithmetic.difference(num1, num2))
    #print(arithmetic.product(num1, num2))
    #print(arithmetic.quotient(num1, num2))
    print(pi)
    
    s1 = objects.Student("Jazelle", "BSIT")
    s1.introduce()
    
    
    


if __name__=="__main__":
    main()