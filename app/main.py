from modules.add_student import AddStudent
from modules.log_in import LogIn
from modules.print_all_student import PrintAllStudents
from modules.search_student import Search
from modules.student import StudentInfo
from modules.main_menu import MainMenu

DB_PATH = "app/student_data.txt"


#initialize the classes
admin = StudentInfo()
student_list = admin.all_student

add_student_service = AddStudent(StudentInfo, student_list, DB_PATH)
log_in_service = LogIn()
print_all_service = PrintAllStudents()
search_service = Search()


add_student_service.read()

access = log_in_service.log_in(student_list)

if access:
      main_menu = MainMenu(add_student_service, print_all_service.print_all_student, search_service.search_student, access)
      main_menu.func()