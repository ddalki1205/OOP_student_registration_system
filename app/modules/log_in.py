import tkinter as tk
from tkinter import messagebox

class LoginScreen:
    def __init__(self, root, db):
        self.root = root
        self.db = db
        self.root.title("Student Registration System - Login")
        self.root.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        self.label_id = tk.Label(self.root, text="Enter Student ID")
        self.label_id.pack(pady=10)

        self.entry_id = tk.Entry(self.root)
        self.entry_id.pack(pady=5)

        self.login_button = tk.Button(self.root, text="Login", command=self.check_login)
        self.login_button.pack(pady=20)

    def check_login(self):
        student_id = self.entry_id.get()
        for student in self.db:
            if student.get_id() == student_id:
                messagebox.showinfo("Login Successful", "Welcome to the system!")
                self.root.destroy()  # Close the login window
                return student  # Return the student object
        messagebox.showerror("Login Failed", "Student ID not found.")
        self.entry_id.delete(0, tk.END)