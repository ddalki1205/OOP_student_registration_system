class LogIn:
    MAX_ATTEMPTS = 4

    def func(self, db, use_gui=False):
        if use_gui:
            # Run GUI login screen if use_gui is True
            from app.modules.log_in_gui import LogInGUI
            import tkinter as tk
            
            root = tk.Tk()
            login_gui = LogInGUI(root, db)
            root.mainloop()
        else:
            # Existing console login method
            return self.console_login(db)

    def console_login(self, db):
        import os
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
                input(f"\nYou have {attempts} more attempts left. Press enter to continue...")
                os.system('cls' if os.name == 'nt' else 'clear')

        os.system('cls' if os.name == 'nt' else 'clear')
        print("Too many failed attempts. Please try again later!")
        return False