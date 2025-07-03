#Condition statements
#if statement
#elif statement
#else statement
#Nested statement

age = int(input("Please enter age: "))

if age >= 18:
    height = int(input("Please enter your height in cm: "))
    if height >= 176:
        print("Tall an legal age")
    elif height >= 150:
        print("Average and legal age")
    else:
        print("Short and legal age")
else:
    print("Too young")

#Not keyword
if not age >= 18:
    print("You are not illegible")
else:
    print("You are illegible")

#Logical Operators AND and  OR
fruit = input("Please input the fruit you have: ")
color = input("Please input the color of fruit: ")

if fruit == "apple" and color == "green":
    print("You brought the needed item!")
elif fruit == "mango" or fruit == "banana" and color == "yellow":
    print("You brought the necessary one!")
else:
    print("Sorry,you did not satisfy the requirement")

#Collection conditional statements
#Used to check an item if it's in a collection(list or tuple)

courses = ("BSIT", "BSCRIM", "BSBA", "BSED")

if "BSIT" in courses:
    print("The item exist!")
else:
    print("Couldn't find the item!")


