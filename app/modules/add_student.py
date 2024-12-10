from tkinter import *
from functools import partial
class AddStudent:
  def __init__(self, constructor, db, path):
    self.constructor = constructor
    self.db = db            #The list in student.py => admin.all_students
    self.path = path        #THE TXT FILE

  def func(self, student): #this deals with adding and writing(don't use before preloading from file)
    self.db.append(student)
    self.write(student)

  def create(self, attributes):
    name, age, id, email, phone = attributes
    new_student = self.constructor(name, age, id, email, phone)
    self.func(new_student)

  def read(self):
    with open(self.path, 'r') as f:
      for line in f:
        attributes = line.strip().split(',')
        student = self.constructor(*attributes)
        self.db.append(student)

  def write(self, student):
    with open(self.path, 'a') as f:
      display = ",".join(student.attributes())
      f.write(f"{display}\n")

  def show_reg_ui(cats, register_frame):
    cats.lblErrors = Label(register_frame, text="", font=("Segoe UI", 18), fg="red")
    cats.lblErrors.grid(row=1, column=0, columnspan=4)
    cats.register_txt = ["Name", "Age", "ID", "Email", "Phone"]
    cats.reg_entry = []
    for i in range(len(cats.register_txt)):
      Label(register_frame, text=cats.register_txt[i], font=("Segoe UI", 18), width=13, anchor="w").grid(row=i+2, column=0)
      cats.reg_entry.append(Entry(register_frame)