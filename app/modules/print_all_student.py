import customtkinter as ctk

class PrintAllStudents:
    def __init__(self, path, constructor):
        self.path = path  
        self.constructor = constructor 

    def func(self):
        try:
            with open(self.path, 'r') as f:
                for line in f:
                    attributes = line.strip().split(',')
                    student = self.constructor(*attributes)  
                    #print(student)
                    yield student
        except FileNotFoundError:
            print("No student data file found.")

    def display(self, view_all_frame):
        print("displaying all students")
        label = ctk.CTkLabel(view_all_frame, text="All students:", font=("Mojang", 20), width=13, anchor="e")
        label.pack(pady=5, padx=20, anchor="w")  

        for student in self.func():
            ctk.CTkLabel(view_all_frame, text=f"{student}", font=("Mojang", 20)).pack(pady=20)