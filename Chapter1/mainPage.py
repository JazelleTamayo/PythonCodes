
from os import system
system('cls')

#Global Variables
y = "World"

#LOCAL VARIABLES
def sayHello():
    x = "Hello"
    print(f"{x} {y}!")

def say(word):
    y = "Damn it!"
    print(y)
    print(word)


def main():
    sayHello()
    say("How are you?")
    print(y)

if __name__=="__main__":
    main()