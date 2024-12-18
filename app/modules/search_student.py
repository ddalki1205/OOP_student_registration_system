import customtkinter as ctk
from tkinter import StringVar
class Search:
    def __init__(self, data_processor):
     self.data_processor = data_processor

    ''' ----------------------------------------------------------------------------------------------------------------- '''
    
    def display(self, search_frame):
        """
        Create the search for students UI.
        """

        label = ctk.CTkLabel(search_frame, text="Search  Student:", font=("Mojang", 23), width=13, text_color="white")
        label.pack(pady=40, padx=20, anchor="s")  

        self.search_input = StringVar(search_frame)
        self.entry = ctk.CTkEntry(search_frame, textvariable=self.search_input , width=600, font=("Segoe UI", 20))
        self.entry.pack(padx=20) 

        self.lblErrors = ctk.CTkLabel(search_frame, text="", font=("Segoe UI", 20), text_color="red")
        self.lblErrors.pack(pady=10)  

        search_btn = ctk.CTkButton(search_frame, width=20, text="Search", font=("Mojang", 17), text_color="white", fg_color="#009047", hover_color="#064d2a", border_spacing=15, corner_radius=0, command=self.check_entries)
        search_btn.pack(pady=10)

        self.display_student_label = ctk.CTkLabel(search_frame, text="")
        self.display_student_label.pack(pady=30)

    def check_entries(self):
        """
        Validate and create a new student from form input.
        """
        entry: str = self.entry.cget("textvariable").get().strip()

        if not entry:
            self.lblErrors.configure(text="Error, wla k nilagay")
            return

        result: object = self.data_processor.fetch_student_by_id(entry)  # if found

        if not result:
            self.lblErrors.configure(text="Error, wla sa db")
            return

        # Get [name, age, id, email, phone]
        student_attributes: list[str] = result.attributes()
        name, age, student_id, email, phone = student_attributes

        self.lblErrors.configure(text="")

        details = (
            f"Name: {name}\n\n"
            f"Age: {age}\n\n"
            f"ID: {student_id}\n\n"
            f"Email: {email}\n\n"
            f"Phone: {phone}"
        )
        self.display_student_label.configure(text=details, font=("Mojang", 20), text_color="white", anchor="w", justify="left")

        