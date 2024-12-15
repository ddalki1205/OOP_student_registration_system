import customtkinter as ctk
from tkinter import StringVar
class Search:
    def __init__(self, path, constructor):
        self.path = path
        self.constructor = constructor  

    def func(self, target_id):
        try:
            with open(self.path, 'r') as f:
                for line in f:
                    attributes = line.strip().split(',')
                    if attributes[2] == target_id:  
                        return self.constructor(*attributes)  
        except FileNotFoundError:
            print("No student data file found.")
        return None
    
    def display(self, search_frame):
        """
        Create the search for students UI.
        """
        self.lblErrors = ctk.CTkLabel(search_frame, text="", font=("Mojang", 20), text_color="red")
        self.lblErrors.pack(pady=10)  
        
        label = ctk.CTkLabel(search_frame, text="Search Student", font=("Mojang", 20), width=13, anchor="e")
        label.pack(pady=5, padx=20, anchor="w")  

        self.search_input = StringVar(search_frame)
        self.entry = ctk.CTkEntry(search_frame, textvariable=self.search_input ,width=40, font=("Mojang", 20))
        self.entry.pack(pady=5, padx=20, fill="x") 

        search_btn = ctk.CTkButton(search_frame, width=30, text="Search",
                                    font=("Mojang", 20), command=self.check_entries)
        search_btn.pack(pady=20)

        self.display_student_label = ctk.CTkLabel(search_frame)
        self.display_student_label.pack(pady=20)

    def check_entries(self):
        """
        Validate and create a new student from form input.
        """
        entry: str = self.entry.cget("textvariable").get().strip()

        if not entry:
            self.lblErrors.configure(text="Error, no input from u")
            return
        
        result: object = self.func(entry) # student object if found

        if not result:
            self.lblErrors.configure(text="Error, could not find student")
            return

        student_attributes: list[str] = result.attributes() #[name, age, id, email, phone]
        name, age, id, email, phone =  student_attributes
        
        self.lblErrors.configure(text="")
        self.display_student_label.configure(text=f"{name}")
        