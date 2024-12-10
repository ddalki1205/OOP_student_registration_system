import tkinter as tk
from modules.add_student import AddStudent
from modules.log_in import LogIn
from modules.print_all_student import PrintAllStudents
from modules.search_student import Search
from modules.student import StudentInfo
from modules.main_menu import MainMenu

DB_PATH = "app/student_data.txt"

admin = StudentInfo()
student_db = admin.all_student

add_student_service = AddStudent(StudentInfo, student_db, DB_PATH)
log_in_service = LogIn()
print_all_service = PrintAllStudents(DB_PATH, StudentInfo)
search_service = Search(DB_PATH, StudentInfo)

add_student_service.read()

access = log_in_service.func(student_db)

if access:
    main_menu = MainMenu(add_student_service, print_all_service.func, search_service.func, access)
    main_menu.func()


