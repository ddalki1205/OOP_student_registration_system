import tkinter as tk
from tkinter import messagebox

class MainMenu:
    def __init__(self, root, user, add_student_service, print_all_service, search_service):
        self.root = root
        self.user = user
        self.add_student_service = add_student_service
        self.print_all_service = print_all_service
        self.search_service = search_service
        self.root.title(f"Welcome, {self.user.get_name()}!")
        self.root.geometry("500x400")
        self.create_widgets()

    def create_widgets(self):
        self.button_view_info = tk.Button(self.root, text="View My Information", command=self.view_my_info)
        self.button_view_info.pack(pady=10)

        self.button_search_student = tk.Button(self.root, text="Search Student Info", command=self.search_student_info)
        self.button_search_student.pack(pady=10)

        self.button_register_new = tk.Button(self.root, text="Register New Student", command=self.register_new_student)
        self.button_register_new.pack(pady=10)

        self.button_print_all = tk.Button(self.root, text="Print All Students", command=self.print_all_students)
        self.button_print_all.pack(pady=10)

        self.button_exit = tk.Button(self.root, text="Exit", command=self.exit_program)
        self.button_exit.pack(pady=10)

    def view_my_info(self):
        info = f"Name: {self.user.get_name()}\nAge: {self.user.get_age()}\nID: {self.user.get_id()}\nEmail: {self.user.get_email()}\nPhone: {self.user.get_phone()}"
        messagebox.showinfo("My Information", info)

    def search_student_info(self):
        student_id = tk.simpledialog.askstring("Search", "Enter Student ID:")
        student = self.search_service.func(student_id)
        if student:
            info = f"Name: {student.get_name()}\nAge: {student.get_age()}\nID: {student.get_id()}\nEmail: {student.get_email()}\nPhone: {student.get_phone()}"
            messagebox.showinfo("Student Information", info)
        else:
            messagebox.showerror("Error", "Student not found.")

    def register_new_student(self):
        new_window = tk.Toplevel(self.root)
        new_window.title("Register New Student")
        new_window.geometry("400x400")

        tk.Label(new_window, text="Name").pack(pady=5)
        entry_name = tk.Entry(new_window)
        entry_name.pack(pady=5)

        tk.Label(new_window, text="Age").pack(pady=5)
        entry_age = tk.Entry(new_window)
        entry_age.pack(pady=5)

        tk.Label(new_window, text="Student ID").pack(pady=5)
        entry_id = tk.Entry(new_window)
        entry_id.pack(pady=5)

        tk.Label(new_window, text="Email").pack(pady=5)
        entry_email = tk.Entry(new_window)
        entry_email.pack(pady=5)

        tk.Label(new_window, text="Phone Number").pack(pady=5)
        entry_phone = tk.Entry(new_window)
        entry_phone.pack(pady=5)

        def add_student():
            name = entry_name.get()
            age = entry_age.get()
            student_id = entry_id.get()
            email = entry_email.get()
            phone = entry_phone.get()
            self.add_student_service.create([name, age, student_id, email, phone])
            messagebox.showinfo("Success", "Student registered successfully!")
            new_window.destroy()

        tk.Button(new_window, text="Register", command=add_student).pack(pady=10)

    def print_all_students(self):
        students_info = self.print_all_service.func()
        messagebox.showinfo("All Students", students_info)

    def exit_program(self):
        self.root.quit()