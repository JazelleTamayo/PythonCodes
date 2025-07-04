#while Loop
#else in while Loop
age = 12

while age < 18:
    print("Still Young: " +str(age))
    age += 1
else:
    print("Legal age: " +str(age))

#while Loop in collections

studentsID = [12, 13, 14, 15, 16, 17]
i = 0

while i < len(studentsID):
    print(studentsID[i])
    i += 1
else:
    print("Not found!")

#Break keyword in while loop

while True:
    print("Hello World")
    break

#Conditions in while loop

print("Do you love your course? ")
while True:
    answer = input("Answer: ")
    if answer == "yes" or answer == "Yes" or answer == "YES":
        print("Good for you")
        break
    elif answer == "no" or answer == "No" or answer == "NO":
        print("Whahaha, you suffer!")
        break
    else:
        print("Please Answer yes or no")

numbers = [1,2,3,4,5,6,7,8]
i = 0

while  i < 7:
    if  numbers[i] % 2 == 0:
        print("even: " +str(numbers[i]))
        i += 1
    else:
        print("odd: " +str(numbers[i]))
        i += 1












