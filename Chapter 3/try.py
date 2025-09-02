#Function

from os import system
system('cls')

num:float = 3.14

def sayWord(name:str, last:str)->None:
    system('cls')
    print(f"My name is {name} {last}.")

def calculate(num1:int, num2:int)->int:
    global num
    num = 0
    return (num1 + num2) * num

def main():
    try:
        firstName:str = str(input("Enter your first name: "))
        lastName:str = str(input("Enter your last name: "))
        
        sayWord(firstName, lastName)
        print(f"The sum is {calculate(34, 60)}.")
        
        
    except Exception as e:
        print(f"Invalid Input: {e}")
    
        
    
if __name__ == "__main__":
    main()