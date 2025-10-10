'''
	Student GUI
'''
import sys
sys.path.insert(0,"db/")
from db.dbhelper import *

import tkinter as tk   #alias-a name representing another name
from tkinter import ttk,messagebox #ttk=themed tkinter

class StudentList:
    def __init__(self)->None:
        self.root = tk.Tk()
        self.root.title('Tamayo, Jazelle BSIT-3 (19877) PYTHON')
        self.root.resizable(False,False)
        self.selected_idno = None
        self.centerwindow()
        self.showlist()
        self.showform()
        self.load_data()
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
        self.tv=ttk.Treeview(self.frame1,column=('idno','name','course','level'),show='headings')
        self.tv.grid(row=0,column=0)
        
        self.tv.bind('<ButtonRelease-1>',self.selectitem)
        
        self.scrollbar.config(command=self.tv.yview)
        
        #define the column sizes and the orientation
        self.tv.column('idno',anchor='c',width=100)
        self.tv.column('name',anchor='w',width=100)
        self.tv.column('course',anchor='w',width=100)
        self.tv.column('level',anchor='c',width=100)
        #define the headings of the columns
        self.tv.heading('idno',text='IDNO')
        self.tv.heading('name',text='NAME')
        self.tv.heading('course',text='COURSE')
        self.tv.heading('level',text='LEVEL')
        
         # Bind selection to load fields ONLY (no DB writes!)
        self.tv.bind('<ButtonRelease-1>', self.selectitem)
        
    def load_data(self) -> None:
        for item in self.tv.get_children():
            self.tv.delete(item)

        students = getall('students')
        for idx, s in enumerate(students):
            self.tv.insert(
                '', 'end', f'item{idx}',
                values=(str(s['idno']), str(s['name']).upper(), str(s['course']).upper(), str(s['level']))
            )

    
    
    def selectitem(self, event) -> None:
        # Which Treeview row is focused?
        curitem = self.tv.focus()
        if not curitem:
            return

        # Get the row dict and extract its 'values' list
        row = self.tv.item(curitem)              # e.g. {'text':'', 'values':[idno, name, course, level], ...}
        vals = row.get('values', [])
        # Optional: print(row)  # for debugging

        # Guard: need at least 4 values (idno, name, course, level)
        if not vals or len(vals) < 4:
            return

        # Unpack and coerce to strings for the widgets
        idno_str   = str(vals[0])
        name_str   = str(vals[1])
        course_str = str(vals[2])
        level_str  = str(vals[3])

        # Fill the form fields (no DB writes here!)
        self.clearform(keep_selection=True)
        self.txt_idno.insert(0, idno_str)
        self.txt_name.insert(0, name_str)
        self.cbo_course.set(course_str)   # Combobox uses .set()
        self.cbo_level.set(level_str)     # Combobox uses .set()

        # Remember we are editing this primary key
        self.selected_idno = idno_str

        self.txt_idno.config(state='disabled')
        
    
    def showform(self)->None:
        self.frame2 = tk.Frame(self.root)
        self.frame2.grid(row=0,column=1)
        #
        lbl_idno=tk.Label(self.frame2,text="IDNO").grid(row=0,column=0,sticky="w",pady=10)
        lbl_name=tk.Label(self.frame2,text="NAME").grid(row=1,column=0,sticky="w",pady=10)
        lbl_course=tk.Label(self.frame2,text="COURSE").grid(row=2,column=0,sticky="w",pady=10)
        lbl_level=tk.Label(self.frame2,text="LEVEL").grid(row=3,column=0,sticky="w",pady=10)
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
        self.delete_button=tk.Button(self.button_frame, text="DELETE", command=self.deletestudent)
        self.delete_button.grid(row=0,column=2,padx=5)

    
    def savestudent(self)->None:
        idno  = self.txt_idno.get().strip()
        name  = self.txt_name.get().strip()
        course= self.cbo_course.get().strip()
        level = self.cbo_level.get().strip()

        if not (idno and name and course and level):
            messagebox.showwarning('WARNING','FILL ALL FIELDS')
            return

        # If editing the same record → UPDATE
        if self.selected_idno and self.selected_idno == idno:
            ok = updaterecord('students', idno=idno, name=name, course=course, level=level)
            message = "STUDENT UPDATED" if ok else "ERROR UPDATING STUDENT"
        else:
            # If ID exists already, ask to update
            existing = get_by_id('students', idno)
            if existing:
                if messagebox.askyesno("CONFIRM", "ID exists. Update this record?"):
                    ok = updaterecord('students', idno=idno, name=name, course=course, level=level)
                    message = "STUDENT UPDATED" if ok else "ERROR UPDATING STUDENT"
                else:
                    return
            else:
                ok = addrecord('students', idno=idno, name=name, course=course, level=level)
                message = "NEW STUDENT ADDED" if ok else "ERROR ADDING STUDENT"

        messagebox.showinfo('INFORMATION', message)
        self.load_data()
        self.clearform()
        
        
    def deletestudent(self)->None:
        idno = self.txt_idno.get().strip() or (self.selected_idno or "")
        if not idno:
            messagebox.showwarning('WARNING', 'Select a student (or click a row) to delete.')
            return

        if not messagebox.askyesno('CONFIRM DELETE', f"Delete student with IDNO '{idno}'?"):
            return

        ok = deleterecord('students', idno)
        if not ok:
            messagebox.showerror('ERROR', 'DELETE FAILED (record may not exist).')
            return

        messagebox.showinfo('INFORMATION', 'STUDENT DELETED')
        self.load_data()
        self.clearform()



    def delete_student(self)->None:  # <<< NEW
        idno = self.txt_idno.get().strip()
        if not idno:
            messagebox.showwarning("WARNING", "Select a record to delete.")
            return
        if not get_by_id('students', idno):
            messagebox.showwarning("WARNING", "Record not found.")
            return
        if messagebox.askyesno("CONFIRM", f"Delete student {idno}?"):
            ok = deleterecord('students', idno)
            messagebox.showinfo("INFORMATION", "STUDENT DELETED" if ok else "ERROR DELETING STUDENT")
            self.load_data()
            self.clearform()
            
    def new_record(self)->None:  # <<< NEW
        self.clearform()
       
    def clearform(self, keep_selection: bool = False) -> None:
        # unlock before modifying text
        self.txt_idno.config(state='normal')

        self.txt_idno.delete(0, tk.END)
        self.txt_name.delete(0, tk.END)
        self.cbo_course.set("")
        self.cbo_level.set("")
        self.txt_idno.focus_set()

        if not keep_selection:
            self.selected_idno = None
    
def main()->None:
    StudentList()    
    
if __name__=="__main__":
    main()