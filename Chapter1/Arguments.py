#Arbitrary Arguments
def sayHello(*names):
    for name in names:
        print("Hello! " +name)


sayHello("Jazelle", "Ejhie", "Joemarie")

#Keyword Arguments
def printFamily(firstName, lastName):
        print(firstName+ " " +lastName)

printFamily(lastName = "Tamayo", firstName = "Joey")

#Arbitratry and keyword Argument together
#Only one arbitrary argument in 1 function
def printSmithFam(*firstName, lastName):
    for name in firstName:
        print(name+ " " +lastName)

printSmithFam("Jazelle", "Ejhie", "Jholia", lastName = "Smith")

#Arbitrary Keyword Argument
def printStudent(**studentInfo):
    print(studentInfo["name"]+ " " +studentInfo["lastName"])
    print(studentInfo["age"])
    print(studentInfo["course"])

printStudent(name = input("Enter First Name: "), lastName = input("Enter Last Name: "), age = int(input("Enter Age: ")), course = input("Enter course: "))