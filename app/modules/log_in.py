import os

class LogIn:
    MAX_ATTEMPTS = 4
    def func(self, db):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Welcome to the Student Information System!")
        attempts = LogIn.MAX_ATTEMPTS

        while attempts > 0:
            studentID = input("Enter your Student ID to access the system: ")

            for student in db:
                if student.get_id() == studentID:
                    return student
            attempts -= 1

            if attempts >= 1:
                input(f"\nYou have {attempts} more attempts left. Please enter to continue...")
                os.system('cls' if os.name == 'nt' else 'clear')

        os.system('cls' if os.name == 'nt' else 'clear')
        print("Too many failed attempts. Please try again later!")
        return False 