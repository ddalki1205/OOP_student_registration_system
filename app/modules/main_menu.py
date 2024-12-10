import tkinter as tk
from tkinter import messagebox


class MainMenu:
    def __init__(self, root, add_student_service, printfunc, searchfunc, user):
        self.root = root
        self.student_service = add_student_service
        self.addfunc = self.student_service.func
        self.createfunc = self.student_service.create
        self.printfunc = printfunc
        self.searchfunc = searchfunc
        self.user = user

        self.create_gui()

    def create_gui(self):
        self.root.title("Student Registration System")
        self.root.geometry("500x300")

        # Left Frame for options
        self.frame_left = tk.Frame(self.root)
        self.frame_left.pack(side="left", padx=20, pady=20)

        # Right Frame for content
        self.frame_right = tk.Frame(self.root)
        self.frame_right.pack(side="right", padx=20, pady=20)

        self.label_title = tk.Label(self.frame_left, text="Main Menu", font=("Arial", 16))
        self.label_title.grid(row=0, column=0, pady=10)

        # Buttons for options
        self.btn_view_info = tk.Button(self.frame_left, text="View My Info", width=20, command=self.check_own_info)
        self.btn_view_info.grid(row=1, column=0, pady=5)

        self.btn_search_student = tk.Button(self.frame_left, text="Search Student Info", width=20, command=self.show_searched_student)
        self.btn_search_student.grid(row=2, column=0, pady=5)

        self.btn_register_student = tk.Button(self.frame_left, text="Register New Student", width=20, command=self.register_new_student)
        self.btn_register_student.grid(row=3, column=0, pady=5)

        self.btn_print_all_students = tk.Button(self.frame_left, text="Print All Students", width=20, command=self.show_all_students)
        self.btn_print_all_students.grid(row=4, column=0, pady=5)

        self.btn_exit = tk.Button(self.frame_left, text="Exit System", width=20, command=self.exit_system)
        self.btn_exit.grid(row=5, column=0, pady=5)

        self.content_display = tk.Label(self.frame_right, text="Welcome to the Main Menu", font=("Arial", 12))
        self.content_display.grid(row=0, column=0, pady=10)

    def display_content(self, text):
        self.content_display.config(text=text)

    def check_own_info(self):
        info = f"=== My Information ===\n{self.user}\n=== Nothing Follows ==="
        self.display_content(info)

    def register_new_student(self):
        name = input("Enter the name: ").strip().replace(',', "")
        age = input("Enter the age: ").strip().replace(',', "")
        student_id = input("Enter the ID: ").strip().replace(',', "")
        email = input("Enter the email: ").strip().replace(',', "")
        num = input("Enter the phone number: ").strip().replace(',', "")

        student = StudentInfo(name, age, student_id, email, num)
        self.createfunc([name, age, student_id, email, num])

        self.display_content(f"Added {name} to the system.\nPress Enter to continue...")

    def show_searched_student(self):
        student_id = input("Enter Student ID to search: ")
        student = self.searchfunc(student_id)

        if student:
            self.display_content(f"=== Student Information ===\n{student}")
        else:
            self.display_content(f"Student with ID {student_id} not found!")

    def show_all_students(self):
        students = "\n".join([str(student) for student in self.student_service.db])
        self.display_content(f"=== All Students Information ===\n{students}")

    def exit_system(self):
        self.root.quit()