#Creating a Functions
def sayHello():
    print("Hello")

#Calling a function
sayHello()

#Arguments and Parameters

def sayHi(name, lastName):
    print("Hello! " +name+ " " +lastName)

name = input("Please enter a name: ")
lastName = input("Please enter your last name: ")
sayHi(name, lastName)


#Return values
def calculate(num1, num2):
    return num1 + num2

sum = calculate(5,10)
print(sum)

def isLegalAge(age):
    if age > 18:
        result = "Legal Age"
        return result
    else:
        result = "Minor"
        return result

age = input("Please enter age: ")
result = isLegalAge(int(age))
print(str("You are in " +result))

