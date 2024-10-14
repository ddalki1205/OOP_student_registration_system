import os

class LogIn:
   MAX_ATTEMPTS = 4
   def log_in(self, student_list):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to the Student Information System!")
    attempts = LogIn.MAX_ATTEMPTS

    while attempts > 0:
      studentID = input("Enter your Student ID to access the system: ")

      for student in student_list:
        if student.get_id() == studentID:
          return student
      attempts -= 1

      input(f"\nYou have {attempts} more attempts left. Please enter to continue...")
      os.system('cls' if os.name == 'nt' else 'clear')

    print("Too many failed attempts. Please try again later!")
    return False 