'''
	StudentList
'''
from student import Student

class StudentList:
    def __init__(self,size)->None: 
        self.slist = [] #data container
        self.size = size
        
    #sentinel modules
    def isempty(self)->bool:    return len(self.slist)==0
    def isfull(self)->bool:     return len(self.slist)==self.size
    #utility modules
    def addstudent(self,s:Student)->bool:
        ok:bool=not self.isfull()
        if ok:
            self.slist.append(s)
        return ok
            
    def findstudent(self,idno:str)->Student:
        ok:bool = not self.isempty()
        if ok:
            for student in self.slist:
                if student.getidno() == idno:
                    return student
                    break
        return None
        
    def deletestudent(self,idno:str)->bool:
        ok:bool = False
        student:Student = self.findstudent(idno)
        if student != None:
            self.slist.remove(student)
            ok=True
        return ok
            
    def updatestudent(self,s:Student)->bool:
        ok:bool = False
        student:Student = self.findstudent(s.getidno())
        if student != None:
            index:int = self.slist(student)
            self.slist[index]=s
            ok=True
        return ok
        
    def showlist(self) -> None:
        if self.isempty():
            print(" "*25 + "No students found.")
        else:
        # header
            header = f"{'IDNO':<10} {'LASTNAME':<15} {'FIRSTNAME':<15} {'COURSE':<10} {'LEVEL':<5}"
            print(header.center(73))
            print(("-"*60).center(73))

        # rows
            for student in self.slist:
                line = f"{student.getidno():<10} {student.getlastname():<15} {student.getfirstname():<15} {student.getcourse():<10} {student.getlevel():<5}"
                print(line.center(73))



