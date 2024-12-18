import os
from modules.student import StudentInfo

class LogIn:
    MAX_ATTEMPTS = 4
    
    def __init__(self, students_file):
        self.students_file = students_file
        self.db = self.load_students()  
        self.attempts = LogIn.MAX_ATTEMPTS  

    def load_students(self):
        students = []
        print("Initializing DB with student data...")
        try:
            with open(self.students_file, "r") as file:
                for line in file:
                    print(line)
                    print(f"Reading line: {line.strip()}")  # Debug line
                    attributes = line.strip().split(',')
                    if len(attributes) == 5:
                        name, age, student_id, email, phone = attributes
                        student = StudentInfo(name, age, student_id, email, phone)
                        students.append(student)
                        print(f"Loaded student: {student.get_id()}")  # Debug loaded student ID
        except FileNotFoundError:
            print("Student data file not found.")
        return students

    def func(self, db):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Welcome to the Student Information System!")
        attempts = LogIn.MAX_ATTEMPTS

        while attempts > 0:
            studentID = input("Enter your Student ID to access the system: ")

            student = self.validate_credentials(studentID)

            if student:
                return student
            attempts -= 1

            if attempts >= 1:
                input(f"\nYou have {attempts} more attempts left. Please enter to continue...")
                os.system('cls' if os.name == 'nt' else 'clear')

        os.system('cls' if os.name == 'nt' else 'clear')
        print("Too many failed attempts. Please try again later!")
        return False

    def validate_credentials(self, studentID):
        studentID = studentID.strip().lower()  
        print(f"Searching for student {studentID} in DB...")  # Debug
        print(self.db)
        for student in self.db:
            print(f"Checking against: {student.get_id().strip().lower()}")  # Debug each check
            if student.get_id().strip().lower() == studentID:
                return student
        return None