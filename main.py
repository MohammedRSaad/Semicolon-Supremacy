import datetime as dt
import pandas as pd
import tkinter as tk

class students:
    def __init__(self, Id, name):
        self.info = [Id, name]

class classrooms:
    def __init__(self, name):
        self.name = name
        self.students = pd.DataFrame(columns=["id", "name"])
    
    def add_student(self, Id, name): #object from student class
        student = students(Id, name)
        self.students.loc[self.students.shape[0]+1] = student.info
    
    def remove_student(self, student):
        self.students.drop(self.students.index[self.students["id"] == student[0]], inplace = True)
    
    def take_attendence(self, name=None):
        date = dt.datetime.now().strftime("%Y-%m-%d") #if you want to test add: %H:%M:%S
        last = str(self.students.columns.values[-1])
        
        if last == "name" or date > last:
            self.students[f"{date}"] = [1] * len(self.students)
        
        self.students[f"{date}"][self.students['name'] == name] = 0
    
    def get_attendence(self):
        return self.students.iloc[:, 2:].sum(axis=1)

class schools:
    def __init__(self):
        self.classes = []
        self.names = []
    def add_classroom(self, name):
        self.names.append(name)
        a = classrooms(name)
        self.classes.append(a)
    def show_classrooms(self):
        for room in self.classes:
            print (room.students)
            print (room.name)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Attendence Management")
        self.geometry('500x300')
        
    def main_win(self, school):
        self.main = tk.Frame(self)
        self.main.pack(fill="both", expand = True)
        
        new_classroom = tk.Button(self.main, text='New Classroom', command=lambda:\
                      [self.new_classroom_win(school), self.main.pack_forget()])
        new_classroom.grid(column=0, row=0, sticky=tk.E, padx=5, pady=5)
        
        new_student = tk.Button(self.main, text='Add Student', command=lambda:\
                      [self.add_student_win(school), self.main.pack_forget()])
        new_student.grid(column=0, row=1, sticky=tk.E, padx=5, pady=5)
        
        show = tk.Button(self.main, text='show Classrooms', command=lambda:\
                      [school.show_classrooms()])
        show.grid(column=0, row=2, sticky=tk.E, padx=5, pady=5)
    
    def new_classroom_win(self, school):
        self.new_classroom = tk.Frame(self)
        self.new_classroom.pack(fill="both", expand = True)

        label = tk.Label(self.new_classroom, text="Class Name: ")
        label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        name = tk.Entry(self.new_classroom)
        name.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)
        
        submit = tk.Button(self.new_classroom, text='submit', command=lambda:\
                      [school.add_classroom(name.get())])
        submit.grid(column=2, row=3, sticky=tk.E, padx=5, pady=5)
        
        main_menu_button = tk.Button(self.new_classroom, text='Main Menu', command=lambda:\
                      [self.main_win(school), self.new_classroom.pack_forget()])
        main_menu_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)
        
    def add_student_win(self, school):
        self.new_student = tk.Frame(self)
        self.new_student.pack(fill="both", expand = True)

        label = tk.Label(self.new_student, text="Class Name: ")
        label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        name_var = tk.StringVar()
        name_var.set("choose")
        name = tk.OptionMenu(self.new_student, name_var, *school.names if school.names else ["No classes"])
        name.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)
        
        
        label = tk.Label(self.new_student, text="ID: ")
        label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
        Id = tk.Entry(self.new_student)
        Id.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)
        
        label = tk.Label(self.new_student, text="Name: ")
        label.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
        name = tk.Entry(self.new_student)
        name.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)
        
        submit = tk.Button(self.new_student, text='submit', command=lambda:\
                      [school.classes[school.names.index(name_var.get())].add_student(Id.get(), name.get())])
        submit.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)
        
        main_menu_button = tk.Button(self.new_student, text='Main Menu', command=lambda:\
                      [self.main_win(school), self.new_student.pack_forget()])
        main_menu_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)
    

if __name__ == "__main__":
    app = App()
    school = schools()
    app.main_win(school)
    app.mainloop()
