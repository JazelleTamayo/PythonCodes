
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"I am {self.name}")



def main():
    p1 = Person("Jazelle")
    p2= Person("Ejhie")
    p3 = Person("Joemarie")

    listOfPeople = [p1, p2, p3]
    for person in listOfPeople:
        person.introduce()

    print("\n")
    emptyList = []
    for i in range(3):
        name = input("Enter name: ")
        p = Person(name)
        emptyList.append(p)


    for person in emptyList:
        person.introduce()



if __name__ == "__main__":
    main()