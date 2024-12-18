import os
import random
from PIL import Image, ImageTk
import customtkinter as ctk
from tkinter import StringVar

class Search:
    def __init__(self, data_processor):
        self.data_processor = data_processor
        self.student_image = None  

    ''' ----------------------------------------------------------------------------------------------------------------- '''
    
    def get_random_image(self, folder_path):
        files = os.listdir(folder_path)
        image_files = [file for file in files if file.endswith(('.png', '.jpg'))]
        if not image_files:
            raise FileNotFoundError("No image files found in the specified folder.")
        random_image = random.choice(image_files)
        return os.path.join(folder_path, random_image)

    def display(self, search_frame):
        # Title
        label = ctk.CTkLabel(search_frame, text="Search Student by ID:", font=("Mojang", 23), width=13, text_color="white")
        label.pack(pady=40, padx=20, anchor="s")  

        # Entry
        self.search_input = StringVar(search_frame)
        self.entry = ctk.CTkEntry(search_frame, textvariable=self.search_input, width=600, font=("Segoe UI", 20))
        self.entry.pack(padx=20) 

        # Errors
        self.lblErrors = ctk.CTkLabel(search_frame, text="", font=("Segoe UI", 20), text_color="red")
        self.lblErrors.pack(pady=10)  

        # Search button
        search_btn = ctk.CTkButton(search_frame, width=20, text="Search", font=("Mojang", 17), text_color="white", fg_color="#009047", hover_color="#064d2a", border_spacing=15, corner_radius=0, command=self.check_entries)
        search_btn.pack(pady=10)

        # Student results
        self.display_student_label = ctk.CTkLabel(search_frame, text="")
        self.display_student_label.pack(pady=30)

    def check_entries(self):
        """
        Validate and create a new student from form input.
        """
        entry: str = self.entry.cget("textvariable").get().strip()

        if not entry:
            self.display_student_label.configure(text="", image="")
            self.lblErrors.configure(text="Error, no input provided")
            return

        result: object = self.data_processor.fetch_student_by_id(entry)

        if not result:
            self.display_student_label.configure(text="", image="")
            self.lblErrors.configure(text="Error, student not found in database")
            return

        student_attributes: list[str] = result.attributes()
        name, age, student_id, email, phone = student_attributes

        self.lblErrors.configure(text="")

        details = (
            f"     Name:     {name}\n\n"
            f"     Age:     {age}\n\n"
            f"     ID:     {student_id}\n\n"
            f"     Email:     {email}\n\n"
            f"     Phone:     {phone}"
        )

        # Get random image 
        folder_path = "app/images/face"
        random_image_path = self.get_random_image(folder_path)

        original_image = Image.open(random_image_path)
        resized_image = original_image.resize((200, 200), Image.LANCZOS) 
        student_image = ImageTk.PhotoImage(resized_image)  

        self.display_student_label.configure(
            text=details,
            font=("Mojang", 20),
            text_color="white",
            image=student_image,
            compound="left",
            justify="left"
        )

        self.student_image = student_image