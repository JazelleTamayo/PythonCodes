#Inheritance
#Overriding Constructor
#Parent class
class Person:
    def __init__(self, fName, lName):
        self.fName = fName
        self.lName = lName

    def introduce(self):
        print(f"\nHi! I am {self.fName} {self.lName}")

#Child Class
#Adding attributes
#Function of child class will override the parent class if it is called
class Student(Person):
    def __init__(self, fName, lName, section):
        super().__init__(fName, lName)
        self.section = section

    def introduce(self):
        super().introduce()

    def saySection(self):
        print(f"From {self.section}")


class Employee(Student):
    def __init__(self, fName, lName, section, salary):
        super().__init__(fName, lName, section)
        self.salary = salary

    def introduce(self):
        super().introduce()

    def saySection(self):
        super().saySection()

    def saySalary(self):
        print(f"Salary: {self.salary}")

#objects
def main():
    one = Person("Jazelle", "Tamayo")
    one.introduce()

    sOne = Student("Sasa", "Tamayo", "BSIT-3B")
    sOne.introduce()
    sOne.saySection()

    eOne = Employee("Ejhie", "Pacs", "BSIT-3B", 36000)
    eOne.introduce()
    eOne.saySection()
    eOne.saySalary()



if __name__ == "__main__":
    main()