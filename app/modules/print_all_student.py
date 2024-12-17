import customtkinter as ctk
from CTkTable import *


class PrintAllStudents:
    def __init__(self, data_processor):
        self.data_processor = data_processor
    
    ''' ---------------------------------------------------------------------------------------------------------------
    *
    *
    *   OLD FUNCTIONS FEEL FREE TO REMOVE THESE ARE THEY ARE SUPERSEDED BY THE DATA_PROCESSOR CLASS WHICH HANLES IT NOW
    *
    *
    * ----------------------------------------------------------------------------------------------------------------- ''' 
    def func(self):
        pass
        try:
            with open(self.path, 'r') as f:
                for line in f:
                    attributes = line.strip().split(',')
                    student = self.constructor(*attributes)  
                    #print(student)
                    yield student
        except FileNotFoundError:
            print("No student data file found.")
    ''' ----------------------------------------------------------------------------------------------------------------- '''

    def display(self, view_all_frame):
        print("displaying all students")
        frame = ctk.CTkScrollableFrame(view_all_frame)
        frame.pack(expand=True, fill="both")
        label = ctk.CTkLabel(frame, text="All students:", font=("Mojang", 20), width=13, anchor="e")
        label.pack(pady=5, padx=20, anchor="w")  

        data_table = []
        data_table.append(['ID', 'Name', 'Age', 'Email', 'Phone']) # adding the header

        for student in self.data_processor.students.values():
            print(f"Adding to the table {student.name}")
            name, age, id, email, phone = student.attributes()
            row = [id, name, age, email, phone]
            data_table.append(row)
        
        table = CTkTable(master=frame, row=len(data_table), column=len(data_table[1]), values=data_table)
        table.pack(expand=True, fill="both", padx=20, pady=20)