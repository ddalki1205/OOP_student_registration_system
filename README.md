## README
- Program allows you to store information of students
- allows you to read and add information

## Project Overview
Student Management System - console-based application that allows for the management of student information.

Users can add new students, view student details, search for specific students, and print all student records.

## LAYOUT
```
student_registration_system/                                      root folder of the application
│
├── app/
│   ├── modules                           all the services of the program
│   │     ├── add_student.py              contains the function to add student, create student, read and write to file.
│   │     ├── log_in.py                   deals with auth
│   │     ├── student.py                  data model for users, => encapsulation, classes, operations &c.
│   │     ├── print_all-students.py       function to print all students in db
│   │     ├── search_student.py           function to search student through db(not yet fully implemented)
│   │     └── main_menu.py                controller for UI and application flow
│   │ 
│   ├── main.py                           main entry point for the application
│   └── student_data.txt                  file for storing student data
└── 
```