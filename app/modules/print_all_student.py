import customtkinter as ctk
from CTkTable import *


class PrintAllStudents:
    def __init__(self, data_processor):
        self.data_processor = data_processor
    
    ''' ----------------------------------------------------------------------------------------------------------------- '''

    def display(self, view_all_frame):
        print("displaying all students")
        frame = ctk.CTkScrollableFrame(view_all_frame, fg_color="#303030")
        frame.pack(expand=True, fill="both")

        label = ctk.CTkLabel(frame, text="All students:", font=("Mojang", 26), text_color="white", corner_radius=0, width=10)
        label.pack(pady=30, anchor="n")  

        data_table = []
        data_table.append(['ID', 'Name', 'Age', 'Email', 'Phone']) 

        for student in self.data_processor.students.values():
            print(f"Adding to the table {student.name}")
            name, age, id, email, phone = student.attributes()
            row = [id, name, age, email, phone]
            data_table.append(row)
        
        table = CTkTable(master=frame, row=len(data_table), column=len(data_table[1]), values=data_table, corner_radius=0)
        table.pack(expand=True, fill="both", padx=20, pady=5)