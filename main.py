import datetime as dt
import pandas as pd
import time

class students:
    def __init__(self, Id, name):
        self.info = [Id, name]

class classroom:
    def __init__(self, grade, number):
        self.grade = grade
        self.number = number
        self.students = pd.DataFrame(columns=["id", "name"])
        self.last_day = open('last_day.txt', "r+")
        date = dt.datetime.now()
        date = (date - dt.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
        self.last_day.write(f"{date}")
    
    def add_student(self, student): #object from student class
        self.students.loc[self.students.shape[0]+1] = student
    
    def remove_student(self, student):
        self.students.drop(self.students.index[self.students["id"] == student[0]], inplace = True)
    
    def take_attendence(self, ids=None):
        date = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        last = self.last_day.read()
        if date > last:
            self.students[f"{date}"] = [1] * len(self.students)
            self.last_day.truncate()
            self.last_day.write(f"{date}")
        self.students[f"{date}"][ids] = 0
    
    def get_attendence(self):
        return self.students.iloc[:, 2:].sum(axis=1)

s1 = students(12, "mohammed")
s2 = students(23, "ali")
s3 = students(45, "hasan")

a = classroom(10, "A")

a.add_student(s1.info)
a.add_student(s2.info)
a.add_student(s3.info)

a.take_attendence([])
time.sleep(2)
a.take_attendence([3])


#a.remove_student(s1.info)
print(a.get_attendence())

