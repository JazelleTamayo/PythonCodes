#Dictionary
studentOne = {"name":"Jazelle", "sex":"Female", "age":20}
studentTwoAttributes = {"height":172, "weight" : 18}
studentTwo = {"name":"Lindth", "sex":"Male", "age":19, "physical":studentTwoAttributes}

#Reading the whole dictionary
print(studentOne)

#Reading dictionary items
print(studentOne["name"])
print(studentOne["age"])
print(studentTwo["name"])
print(studentTwo["age"])


#Reading Dictionary items using get
print(studentOne.get("sex"))
print(studentTwo.get("sex"))

#Changing the value in the dictionary
studentOne["name"] = "Ejhie"
print(studentOne.get("name"))

#Check the length of dictionary
print(len(studentOne))

#Dictionary add items where the key still does not exist
studentOne["course"] = "BSIT"
studentTwo["course"] = "HM"

print(studentOne)
print(studentTwo)

#Delete using pop()
studentOne.pop("sex")
print(studentOne)

#Delete the last item in the dictionary
studentTwo.popitem()
print(studentTwo)

#Copying the dictionary
student = studentOne.copy()
print(student)

#Getting all keys in the dictionary
print(studentOne.keys())

#Getting all the values in the dictionary
print(studentTwo.values())

#List of Dictionaries
listDict = [studentOne, studentTwo]
print(listDict)

#Access
print(listDict[0].get("name"))
print(listDict[1].get("age"))

#Nested Dictionaries
print(studentTwo.get("physical").get("height"))

#Clear Dictionary
studentOne.clear()
print(studentOne)




