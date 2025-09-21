'''
Student information management
'''
from os import system
from student import Student
filename:str = 'student.csv'
slist:list = []  #local data container, not persistent
#displaymenu
def displaymenu()->None:
    system('cls')
    '''
        create a centered menu program here
    '''
    for i in range(1,5):print(" "*80)
    print(("="*50).center(80, " "))
    print(" STUDENT INFORMATION MANAGEMENT SYSTEM ".center(80," "))
    print(("="*50).center(80, " "))
    print("1. Add New Student Record    ".center(80," "))
    print("2. View All Student Records  ".center(80," "))
    print("3. Search Student Record     ".center(80," "))
    print("4. Update Student Record     ".center(80," "))
    print("5. Delete Student Record     ".center(80," "))
    print("0. Exit                      ".center(80," "))
    print(("="*50).center(80, " "))  
    
       
#file management modules
def load()->None: 
    temp: list = []
    slist.clear()
    file = open(filename)   # original style
    for item in file:
        temp.append(item.strip())
    for data in temp:
        fields: list = data.split(',')
        if len(fields) == 5:   # safeguard if line is malformed
            slist.append(Student(fields[0], fields[1], fields[2], fields[3], fields[4]))
    file.close()

    
def updater()->None:
    file = open(filename, "w")
    if len(slist) > 0:
        for student in slist:
            file.write(student.__str__() + "\n")
    file.close()
            
    
    
#utility modules
def addrecord(student:Student)->bool:
    load()
    slist.append(student)
    updater()
    return True
    
    
    
def findrecord(idno:str)->Student:
    load()
    for student in slist:
        if student.idno == idno:
            return student
    return "Not Found"
           
        
    
    
def deleterecord(idno:str)->bool:
    ok: bool = False
    student = findrecord(idno)
    if student != "Not Found":
        slist.remove(student)
        ok = True     # fixed bug (was `bool = True`)
        updater()
    return ok
    
    
def updaterecord(student:Student)->bool:
    ok: bool = False
    load()
    for s in slist:
        if student.idno == s.idno:
            index: int = slist.index(s)
            slist[index] = student
            ok = True
            updater()   # fixed: now updates file
            break
    return ok
 
 
# display all data
def displaylist()->None:
    system('cls')
    load()
    for i in range(1,5): print(" "*80)
    if len(slist) > 0:
        print(("="*50).center(80, " "))
        print("STUDENT RECORDS".center(80," "))
        print(("="*50).center(80, " "))
        for student in slist:
            print((str(student) + "         ").center(80, " "))
        print(("="*50).center(80, " "))
    else:
        print("List is empty".center(80," "))

    
#default entry module
def main()->None:
    option:str = ""
    while option != '0':
        displaymenu()
        print(" "*25,end="")
        '''
            create a match-case menu selector here
        '''
        option = input("Enter option: ")

        if option == '1':   # Add
            system('cls')
            for i in range(1,5):print(" "*80)
            print(("="*50).center(80, " "))
            print(" ADD NEW STUDENT ".center(80," "))
            print(("="*50).center(80, " "))
            
            # Input loop for ID
            while True:
                print(" "*25, end="")
                idno = input("Enter ID:         ").strip()
                if idno == "":
                    print("ID cannot be empty.".center(80," "))
                    continue
                if findrecord(idno) != "Not Found":
                    print(f"{' '*25}Student ID {idno} already exists.")
                    continue
                break
                
            # Input loop for Last Name
            while True:
                print(" "*25, end="")
                lname = input("Enter Last name:  ").strip()
                if lname == "":
                    print("Last name cannot be empty.".center(80," "))
                    continue
                break
                
            # Input loop for First Name
            while True:
                print(" "*25, end="")
                fname = input("Enter First name: ").strip()
                if fname == "":
                    print("First name cannot be empty.".center(80," "))
                    continue
                break
            
            # Input loop for Course
            while True:
                print(" "*25, end="")
                course = input("Enter Course:     ").strip()
                if course == "":
                    print("Course cannot be empty.".center(80," "))
                    continue
                break
            
            # Input loop for Year/Level
            while True:
                print(" "*25, end="")
                year = input("Enter Year:       ").strip()
                if year == "":
                    print("Year cannot be empty.".center(80," "))
                    continue
                if not year.isdigit():
                    print("Year must be a number.".center(80," "))
                    continue
                break
            
            print(("="*50).center(80, " "))
            addrecord(Student(idno, lname, fname, course, year))
            print("Record added.".center(80," "))           

        elif option == '2':   # View All
            displaylist()

        elif option == '3':   # Search
            system('cls')
            for i in range(1,5):print(" "*80)
            print(("="*50).center(80, " "))
            print("FIND STUDENT".center(80," "))
            print(("="*50).center(80, " "))
            print(" "*25,end="")
            idno = input("Enter ID to find: ")
            student = findrecord(idno)
            print("\n" + " "*24,"Student Info: ") 
            if student != "Not Found":
                print(str(student).center(80, " "))
            else:
                print("Record not found.".center(80," "))
            print(("="*50).center(80, " "))

        elif option == '4':   # Update
            system('cls')
            for i in range(1,5):print(" "*80)
            print(("="*50).center(80, " "))
            print("UPDATE STUDENT".center(80," "))
            print(("="*50).center(80, " "))
            
            print(" "*25,end="")            
            idno = input("Enter ID to update: ").strip()
            
            # Find the existing student
            student = findrecord(idno)
            if student == "Not Found":
                print("Record not found.".center(80," "))
            else:
        # Ask for new values, keep old values if input is empty
                print(" "*25,end="")
                lastname = input(f"Enter New Last name [{student.lastname}]: ").strip()
                if lastname == "":
                    lastname = student.lastname
              
                print(" "*25,end="")
                firstname = input(f"Enter New First name [{student.firstname}]: ").strip()
                if firstname == "":
                    firstname = student.firstname
                 
                print(" "*25,end="")
                course = input(f"Enter New Course [{student.course}]: ").strip()
                if course == "":
                    course = student.course
            
                print(" "*25,end="")
                level = input(f"Enter New Year [{student.level}]: ").strip()
                
                # Validate year input
                if level == "":
                    level = student.level
                elif not level.isdigit():
                    print("Invalid level input. Keeping old value.".center(80," "))
                    level = student.level
                print("\n")
                print(("="*50).center(80, " "))
                
                if updaterecord(Student(idno, lastname, firstname, course, level)):
                    print("Record updated.".center(80," "))
                else:
                    print("Error updating record.".center(80," "))
                            

        elif option == '5':   # Delete
            system('cls')
            for i in range(1,5):print(" "*80)
            print(("="*50).center(80, " "))
            print("DELETE STUDENT".center(80," "))
            print(("="*50).center(80, " "))
            
            print(" "*25,end="")
            idno = input("Enter ID to delete: ")
            print(("="*50).center(80, " "))
            print("\n")
            if deleterecord(idno):
                print("Record deleted.".center(80," "))
            else:
                print("Record not found.".center(80," "))

        elif option == '0':
            print("Exiting program...".center(80," "))

        else:
            print("Invalid option!".center(80," "))
            
        print("\n" + " " * 25, end="")
        input("Press Enter to continue...")
        
            
#application launcher
if __name__=="__main__":
    main()