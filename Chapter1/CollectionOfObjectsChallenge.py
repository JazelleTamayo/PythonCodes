class Student:
    def __init__(self, name, course, year, section):
        self.name = name
        self.course = course
        self.year = year
        self.section = section

    def introduce(self):
                print(f"Name   : {self.name}")
                print(f"Course : {self.course}")
                print(f"Year   : {self.year}")
                print(f"Section: {self.section}")
                print("\n")



def main():
    studentList =  []
    while True:
        print("\n")
        name = input("Enter name of student: ")
        course = input("Enter Course: ")
        year = int(input("Enter year : "))
        section = input("Enter section: ")
        stud = Student(name, course, year, section)
        print("Student Created......")
        studentList.append(stud)

        option = input("Create another Student?(Y/N) ")
        if option == 'Y' or option == 'y':
            pass
        else:
            break
    print("\n")


    i = 1
    for person in studentList:
            print(f"Student #{i}")
            i = i + 1
            person.introduce()



if __name__ == "__main__":
    main()