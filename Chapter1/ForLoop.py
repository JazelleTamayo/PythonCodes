#for loop
#else in for loop
#condition in loop

fruits = ["Apple", "Banana", "Orange", "Grapes"]

for item in fruits:
    print(item)
    if item == "Orange":
        print("Oh! You have an orange!")
    elif item == "Grapes":
        print("Oh! You have a grapes!")
    else:
        print("You don't have orange or apple")

else:
    print("No more Fruits")

numbers = [1,2,3,4,5,6,7,8,9,10]

for num in numbers:
    if num % 2 == 0:
        print("Even Number: " +str(num))
    else:
        print("Odd Number: " +str(num))

#Range() in for Loop
for word in range(10):
    print("Hello World")





