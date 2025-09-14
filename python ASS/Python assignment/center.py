'''
	centering the menu'
'''
from os import system
from studentlist import StudentList
from student import Student

slist = StudentList(10)

def displaymenu()->None:
    system('cls')
    for i in range(1,5):print(" "*73)    
    print("       MAIN MENU        ".center(73," "))
    print(" -----------------------".center(73," "))
    print(" 1. ADD STUDENT         ".center(73," "))
    print(" 2. FIND STUDENT        ".center(73," "))
    print(" 3. DELETE STUDENT      ".center(73," "))
    print(" 4. UPDATE STUDENT      ".center(73," "))
    print(" 5. DISPLAY ALL STUDENT ".center(73," "))
    print(" 0. QUIT/END            ".center(73," "))
    print(" -----------------------".center(73," "))
    #for i in range(1,5):print(" "*73)
    
def addstudent()->None:
    system('cls')
    for i in range(1,5):print(" "*73)
    print("      Add Student     ".center(73))
    print("----------------------".center(73))
    
    # --- IDNO ---
    while True:
        print(" "*25, end="")
        idno:str = input("IDNO      :   ").strip()
        if not idno:
            print(" "*25 + "Error: ID cannot be empty.")
        elif not idno.isdigit():
            print(" "*25 + "Error: ID must be numbers only.")
        else:
            break

    # --- LASTNAME ---
    while True:
        print(" "*25, end="")
        lastname:str = input("LASTNAME  :   ").strip()
        if not lastname:
            print(" "*25 + "Error: Lastname cannot be empty.")
        elif not lastname.isalpha():
            print(" "*25 + "Error: Lastname must contain letters only.")
        else:
            break

    # --- FIRSTNAME ---
    while True:
        print(" "*25, end="")
        firstname:str = input("FIRSTNAME :   ").strip()
        if not firstname:
            print(" "*25 + "Error: Firstname cannot be empty.")
        elif not firstname.isalpha():
            print(" "*25 + "Error: Firstname must contain letters only.")
        else:
            break

    # --- COURSE ---
    while True:
        print(" "*25, end="")
        course:str = input("COURSE    :   ").strip()
        if not course:
            print(" "*25 + "Error: Course cannot be empty.")
        else:
            break

    # --- LEVEL ---
    while True:
        print(" "*25, end="")
        level:str = input("LEVEL     :   ").strip()
        if not level:
            print(" "*25 + "Error: Level cannot be empty.")
        elif not level.isdigit():
            print(" "*25 + "Error: Level must be a number.")
        else:
            break
   
    # Save student
    ok:bool = slist.addstudent(Student(idno,lastname,firstname,course,level))
    print("----------------------".center(73))
    print(" "*25, end="")
    if ok:
        print("Student added successfully!")
    else:
        print("\nFailed to add student.")

   
def findstudent() -> None:
    system('cls')
    for i in range(1,5): print(" "*73)
    print("       Find Student        ".center(73))
    print(" --------------------------".center(73))
    print(" "*25, end="")
    idno = input("IDNO:   ")

    student = slist.findstudent(idno)

    print(" --------------------------".center(73))
    if student:
        print(" Student Found".center(73))
        print(" "*25 + f"IDNO     : {student.getidno()}")
        print(" "*25 + f"LASTNAME : {student.getlastname()}")
        print(" "*25 + f"FIRSTNAME: {student.getfirstname()}")
        print(" "*25 + f"COURSE   : {student.getcourse()}")
        print(" "*25 + f"LEVEL    : {student.getlevel()}")
    else:
        print(" Student Not Found".center(73))
    print(" --------------------------".center(73))
    
def deletestudent() -> None:
    system('cls')
    for i in range(1,5): print(" "*73)
    print("       Delete Student       ".center(73))
    print(" -------------------------- ".center(73))

    print(" "*25, end="")
    idno = input("IDNO:   ")

    print(" "*25, end="")
    confirmation = input("Confirm delete? (y/n): ")

    print(" -------------------------- ".center(73))
    if confirmation.lower() == 'y':
        if slist.deletestudent(idno):
            print(" "*25 + "Student deleted successfully.")
        else:
            print(" "*25 + "Student not found.")
    else:
        print(" "*25 + "Deletion cancelled.") 

def updatestudent() -> None:
    system('cls')
    for i in range(1,5): print(" "*73)
    print("       Update Student       ".center(73))
    print(" -------------------------- ".center(73))

    print(" "*25, end="")
    idno = input("IDNO:   ")

    student = slist.findstudent(idno)
    if student:
        print()
        print(" "*25 + "Enter new details:")

        print(" "*25, end="")
        lastname = input(f"LASTNAME  ({student.getlastname()}): ").strip() or student.getlastname()

        print(" "*25, end="")
        firstname = input(f"FIRSTNAME ({student.getfirstname()}): ").strip() or student.getfirstname()

        print(" "*25, end="")
        course = input(f"COURSE    ({student.getcourse()}): ").strip() or student.getcourse()

        print(" "*25, end="")
        level = input(f"LEVEL     ({student.getlevel()}): ").strip() or student.getlevel()

        # update the student object
        student.setlastname(lastname)
        student.setfirstname(firstname)
        student.setcourse(course)
        student.setlevel(level)

        print(" -------------------------- ".center(73))
        print(" "*25 + "Student updated successfully.")
    else:
        print(" -------------------------- ".center(73))
        print(" "*25 + "Student Not Found.")
             
    
def displayall() -> None:
    system('cls')
    for i in range(1,5): print(" "*73)
    print("       All Students       ".center(73))
    print(" -------------------------- ".center(73))
    slist.showlist()
    print(("-"*60).center(73))

    
def main()->None:
    
    option:str = ""
    while option !="0":
        displaymenu()
        print(" "*25,end="")
        option=input(" Enter Option(0..5):   ")
        match option:
            case "1": addstudent()
            case "2": findstudent()
            case "3": deletestudent()
            case "4": updatestudent()
            case "5": displayall()
            case "0": print("Program Ended".center(73))
            case   _: print("Invalid Option".center(73))
        print(" "*25,end="")
        print(end="")
        input("press any key to continue...")
            
if __name__=="__main__":
    main()