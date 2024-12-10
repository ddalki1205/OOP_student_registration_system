import tkinter as tk
from modules.add_student import AddStudent
from modules.log_in import LoginScreen
from modules.main_menu import MainMenu
from modules.print_all_student import PrintAllStudents
from modules.search_student import Search
from modules.student import StudentInfo

# Path to your student data file
DB_PATH = "student_data.txt"
student_db = []

# Create instances of the services
add_student_service = AddStudent(StudentInfo, student_db, DB_PATH)
print_all_service = PrintAllStudents(DB_PATH, StudentInfo)
search_service = Search(DB_PATH, StudentInfo)

# Initialize data from the file
add_student_service.read()

# Create the root window for the login screen
root = tk.Tk()
login_screen = LoginScreen(root, student_db)
logged_in_user = login_screen.check_login()

if logged_in_user:
    root = tk.Tk()  # Create a new window for the main menu
    main_menu = MainMenu(root, logged_in_user, add_student_service, print_all_service, search_service)
    root.mainloop()