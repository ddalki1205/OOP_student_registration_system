import os

class MainMenu:  
    def __init__(self, add_student_service, printfunc, searchfunc, user):
        self.student_service = add_student_service
        self.addfunc = self.student_service.func
        self.createfunc = self.student_service.create
        self.printfunc = printfunc
        self.searchfunc = searchfunc
        self.user = user

    @staticmethod
    def cls():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def menu(name):
        print(f"Greetings, {name}! \nPlease choose from the following options: ")
        print(f"\n1. View your information"
              f"\n2. View other student's information"
              f"\n3. Register a new student"
              f"\n4. Print all students in the list"
              f"\n5. Exit the System")

    def func(self):
        MainMenu.cls()
        while True:
            MainMenu.menu(self.user.get_name())
            choice = int(input("\nEnter your choice: "))

            if choice == 5:
                print("Exiting Program")
                break

            if choice == 1:
                self.check_own_info()
            elif choice == 2:
                self.show_searched_student()
            elif choice == 3:
                self.register_new_student()
            elif choice == 4:
                self.show_all_students()
            print("Press enter to continue...")
            MainMenu.cls()

    def check_own_info(self):
        MainMenu.cls()
        print("=== My Information ===")
        print(self.user)
        print("=== Nothing Follows ===")
        input("\nPress enter to continue...")

    def register_new_student(self):
        leave = False
        while leave is not True:
            MainMenu.cls()

            print("=== Add new student ===\n")

            name = input("Enter the name: ").strip().replace(',', "")
            age = input("Enter the age: ").strip().replace(',', "")
            id = input("Enter the ID: ").strip().replace(',', "")
            email = input("Enter the email: ").strip().replace(',', "")
            num = input("Enter the number: ").strip().replace(',', "")

            print("\n=== Nothing Follows ===")
            self.createfunc([name, age, id, email, num])

            print(f"Added '{name}' to the system.\n")

            again = input("Do you wish to add another student? (Y/N): ").strip().lower()
            if again == 'n':
                leave = True

    def show_searched_student(self):
        MainMenu.cls()

        user_input = input("Enter Student ID: ")
        student = self.searchfunc(user_input)  

        if student:
            print("=== Student Information ===")
            print(student)  
            print("===== Nothing Follows =====")
        else:
            print(f"Student ID '{user_input}' not found.")

        input("\nPress enter to continue...")
        MainMenu.cls()

    def show_all_students(self):
        MainMenu.cls()

        print("=== All Students Information ===")
        self.printfunc() 
        print("======= Nothing Follows =======")

        input("\nPress enter to continue...")
        MainMenu.cls()