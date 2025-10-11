'''
	Student GUI
'''
import sys
sys.path.insert(0,"db/")
from db.dbhelper import *

import tkinter as tk   #alias-a name representing another name
from tkinter import ttk,messagebox #ttk=themed tkinter

# --- safe SQL helper (do not change imports / dbhelper) ---
def insert_student(idno: str, name: str, course: str, level: str) -> bool:
    # bypass addrecord() to avoid malformed INSERT
    sql = "INSERT INTO students (`idno`,`name`,`course`,`level`) VALUES (?,?,?,?)"
    return postprocess(sql, [idno, name, course, level])

def update_student(idno: str, name: str, course: str, level: str) -> bool:
    # only update non-PK fields; PK (idno) stays the same
    sql = "UPDATE students SET `name`=?, `course`=?, `level`=? WHERE `idno`=?"
    return postprocess(sql, [name, course, level, idno])

def get_by_id(idno: str):
    recs = getrecord('students', idno=idno)
    return recs if recs else []

class StudentList:
    def __init__(self)->None:
        self.root = tk.Tk()
        self.root.title('TAMAYO, Jazelle BSIT-3 (19877) PYTHON')
        self.root.resizable(False,False)
        self.centerwindow()
        
        self.selected_idno = None
        
        self.showlist()
        self.showform()
        self.root.mainloop() #this line should always be last
        
    def centerwindow(self)->None:
        width:int = 700
        height:int = 350
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x:int = (screen_width-width)//2 #integer divide
        y:int = (screen_height-height)//2 #integer divide
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        
    def showlist(self)->None:
        self.frame1=tk.Frame(self.root)
        self.frame1.grid(row=0,column=0,padx=10,pady=30)
        #create a scrollbar
        self.scrollbar = ttk.Scrollbar(self.frame1,orient="vertical")
        self.scrollbar.grid(row=0,column=1,sticky="ns")
        #
        # NOTE: use "columns" (plural)
        self.tv=ttk.Treeview(self.frame1, columns=('idno','name','course','level'), show='headings')
        self.tv.grid(row=0,column=0)
        
        self.tv.bind('<ButtonRelease-1>',self.selectitem)
        
        # link scrollbar both ways
        self.tv.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.tv.yview)
        
        #define the column sizes and the orientation
        self.tv.column('idno',anchor='c',width=100)
        self.tv.column('name',anchor='w',width=150)
        self.tv.column('course',anchor='w',width=120)
        self.tv.column('level',anchor='c',width=80)
        #define the headings of the columns
        self.tv.heading('idno',text='IDNO')
        self.tv.heading('name',text='NAME')
        self.tv.heading('course',text='COURSE')
        self.tv.heading('level',text='LEVEL')
        #populate the treeview
        students:list = getall('students')
        self.count=0
        for student in students:
            self.tv.insert(
                '','end','item'+str(self.count),
                values=(f"{student['idno']}",f"{student['name'].upper()}",f"{student['course'].upper()}",f"{student['level']}")
            )
            self.count+=1
    
    def selectitem(self, a) -> None:
        curitem = self.tv.focus()
        if not curitem:
            return
        selected_item = self.tv.item(curitem)
        data = selected_item.get('values', [])
        if len(data) < 4:
            return

        # clear and fill fields
        self.clearform()  # this also re-enables ID; we'll disable it after filling
        idno, name, course, level = map(str, data[:4])

        self.txt_idno.insert(0, idno)
        self.txt_name.insert(0, name)
        self.cbo_course.set(course)
        self.cbo_level.set(level)

        # remember we are EDITING this id and lock the ID field
        self.selected_idno = idno
        self.txt_idno.config(state='disabled')

    
    def showform(self)->None:
        self.frame2 = tk.Frame(self.root)
        self.frame2.grid(row=0,column=1)
        #
        tk.Label(self.frame2,text="IDNO").grid(row=0,column=0,sticky="w",pady=10)
        tk.Label(self.frame2,text="NAME").grid(row=1,column=0,sticky="w",pady=10)
        tk.Label(self.frame2,text="COURSE").grid(row=2,column=0,sticky="w",pady=10)
        tk.Label(self.frame2,text="LEVEL").grid(row=3,column=0,sticky="w",pady=10)
        #
        self.txt_idno = tk.Entry(self.frame2,width=23)
        self.txt_idno.grid(row=0,column=1)
        self.txt_name = tk.Entry(self.frame2,width=23)
        self.txt_name.grid(row=1,column=1)
        self.cbo_course = ttk.Combobox(self.frame2,width=20,values=('BSIT','BSCS','BSCJ','BSHM','BSE'))
        self.cbo_course.grid(row=2,column=1)
        self.cbo_level = ttk.Combobox(self.frame2,width=20,values=('1','2','3','4'))
        self.cbo_level.grid(row=3,column=1)
        #create a frame for buttons
        self.button_frame=tk.Frame(self.frame2)
        self.button_frame.grid(row=4,column=0,columnspan=2)
        #
        self.save_button=tk.Button(self.button_frame,text="SAVE",command=self.savestudent)
        self.save_button.grid(row=0,column=0)
        self.new_button=tk.Button(self.button_frame,text="NEW",command=self.clearform)
        self.new_button.grid(row=0,column=1,padx=10)
        self.delete_button=tk.Button(self.button_frame,text="DELETE",command=self.deletestudent)
        self.delete_button.grid(row=0,column=2,padx=5)

    def refresh_list(self) -> None:
        for item in self.tv.get_children():
            self.tv.delete(item)
        students = getall('students')
        self.count = 0
        for s in students:
            self.tv.insert('', 'end', 'item'+str(self.count),
                        values=(s['idno'], s['name'].upper(), s['course'].upper(), s['level']))
            self.count += 1



    def deletestudent(self) -> None:
        idno = self.txt_idno.get().strip()
        if not idno:
            curitem = self.tv.focus()
            if curitem:
                vals = self.tv.item(curitem).get('values', [])
                if vals:
                    idno = str(vals[0])
        if not idno:
            messagebox.showwarning('WARNING', 'Select a student to delete.')
            return

        if not messagebox.askyesno('CONFIRM', f"Delete student with IDNO '{idno}'?"):
            return

        try:
            ok = deleterecord('students', idno=idno)
        except Exception as e:
            messagebox.showerror('ERROR', f'ERROR DELETING STUDENT\n\n{e}')
            return

        if ok:
            messagebox.showinfo('INFORMATION', 'STUDENT DELETED')
            self.refresh_list()
            self.clearform()
        else:
            messagebox.showerror('ERROR', 'DELETE FAILED')
        
        
    def savestudent(self) -> None:
        idno   = self.txt_idno.get().strip()
        name   = self.txt_name.get().strip()
        course = self.cbo_course.get().strip()
        level  = self.cbo_level.get().strip()

        if not (idno and name and course and level):
            messagebox.showwarning('WARNING', 'FILL ALL FIELDS')
            return

        try:
            if self.selected_idno and self.selected_idno == idno:
                # EDIT mode → UPDATE existing record
                ok = update_student(idno, name, course, level)
                msg = "STUDENT UPDATED" if ok else "ERROR UPDATING STUDENT"
            else:
                # ADD mode → INSERT new record
                ok = insert_student(idno, name, course, level)
                msg = "NEW STUDENT ADDED" if ok else "ERROR ADDING STUDENT"
        except Exception as e:
            messagebox.showerror('ERROR', str(e))
            return

        messagebox.showinfo('INFORMATION', msg)

        # Always reflect DB truth in the UI
        self.refresh_list()
        self.clearform()

        
    def clearform(self) -> None:    
        self.txt_idno.config(state='normal')  # re-enable IDNO when adding new
        self.txt_idno.delete(0, tk.END)
        self.txt_name.delete(0, tk.END)
        self.cbo_course.set("")
        self.cbo_level.set("")
        self.txt_idno.focus_set()
        self.selected_idno = None   
    
def main()->None:
    StudentList()    
    
if __name__=="__main__":
    main()

