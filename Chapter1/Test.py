#Print something
print("This is my Practice")

#Declare Variables
firstName = "Jazelle"
lastName = "Tamayo"

#Print Variable
print(firstName)

#Do Concatenation
print("I am " +firstName+ " " +lastName)

#Do Input
num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter another number: "))

sum = num1 + num2
difference = num1 - num2
product = num1 * num2
qoutient = num1 / num2
modulo = num1 % num2

#Do Casting and basic operations from input
print(str(num1)+ "+" +str(num2)+ "=" +str(sum))
print(str(num1)+ "-" +str(num2)+ "=" +str(difference))
print(str(num1)+ "*" +str(num2)+ "=" +str(product))
print(str(num1)+ "/" +str(num2)+ "=" +str(qoutient))
print(str(num1)+ "%" +str(num2)+ "=" +str(modulo))


#Make a List
names = ["Jazelle", "Jhanna", "Karl", "Joemarie", "Ejhie", "Janine"]


#Print the whole List
print(names)

#Print specific item on the list
print(names[1])

#Print specified start index
print(names[3:])


#Print specified end index
print(names[:5])


#Print list item of specified start index to end index
print(names[1:4])


#Change the list item
names[0] = ("Janine")
print(names)

#Check the number of list
print(len(names))

#Check what value repeat
print(names.count("Janine"))


#Add item at the end of the list using append
names.append("Clint")
print(names)


#Add item on the specified index using insert
names.insert(2, "Janelle")
print(names)

#Delete an item on the list using
#remove base on the value
names.remove("Karl")
print(names)


#Deleting item using pop
#Delete base on index
#If index is not specified it will delete the last value
names.pop()
print(names)
names.pop(3)
print(names)


#Deleting using del
#If the index is not specified it delete the lis lead to error
del names[0]
print(names)


#Copying a list
x = names.copy()
print(x)

#Combining the lists
otherNames = ["Jenny", "Lisa", "Rose"]
wholeList = names + otherNames
print(wholeList)


#Combining a list using extend
names.extend(otherNames)
print(names)

#Appending lists
names.append(otherNames)
print(names)


#Reverse list items
names.reverse()
print(names)


# Sort the list
alphabet = ["z", "r", "h", "b"]
alphabet.sort()
print(alphabet)

#Do Nest list
fruits = ["Apple", "Banana", "Cacao",["Mango", "Kiwi"]]
print(fruits[3][0])

#Do tuple
print(tuple(fruits))

#Clearing list
names.clear()
print(names)