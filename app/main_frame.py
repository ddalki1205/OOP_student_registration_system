import customtkinter as ctk

from modules.add_student import AddStudent
from modules.student import StudentInfo
from modules.search_student import Search
from modules.print_all_student import PrintAllStudents

class MainFrame(ctk.CTkFrame):
    def __init__(self, parent, students_file):
        super().__init__(parent.root, fg_color="white", bg_color="black")
        self.parent = parent
        self.students_file = students_file

        self.container = []
        self.buttons = []
        self.btn_txt = ["View Profile", "Search Student", "View Students", "Register Student", "Log Out"]

        self.add_student_instance = AddStudent(StudentInfo, self.students_file)
        self.search_student_instance = Search(self.students_file, StudentInfo)
        self.print_all_students_instance = PrintAllStudents(self.students_file, StudentInfo)

        self.create_widgets()

    def create_widgets(self):
        # Sidebar menu
        menu_container = ctk.CTkFrame(self, fg_color="#1e1e1e", bg_color="#1e1e1e")
        menu_container.pack(fill="y", side="left")

        # Content area
        self.content_frame = ctk.CTkFrame(self, fg_color="#303030", bg_color="#303030")
        self.content_frame.pack(fill="both", expand=True, side="right")

        for i in range(len(self.btn_txt) - 1):
            frame = ctk.CTkFrame(self.content_frame, fg_color="#303030")
            ctk.CTkLabel(frame, text=self.btn_txt[i], text_color="white", font=("Minercraftory", 30), width=30, anchor="center").pack(pady=20)
            self.container.append(frame)

        '''
        @ihni - I am refactoring this because you shouldn't be calling the function immediately after frame is created.
        Only call its function when the respective navbar button is pressed.
        - It would be best to refactor and seperate out the functions as a single controller or a combination of multiple ones

        '''
        button_actions = [
            self.show_profile,     # View Profile button
            self.search_students,  # Search Student button
            self.view_students,    # View Students button
            self.register_student, # Register Student button
            self.logout_confirm    # Log Out button
        ]

        for i, action in enumerate(button_actions):
            btn = ctk.CTkButton(
                menu_container,
                text=self.btn_txt[i],
                font=("Mojang", 15),
                fg_color="#008542",
                hover_color="#064d2a",
                width=220,
                height=55,
                command=action,
                anchor="w"
            )
            btn.grid(row=i, column=0, pady=5)
            self.buttons.append(btn)

    def show_profile(self):
        self.open_frame(self.container[0])
        self.add_student_instance.show_student_ui(self.container[0], self.parent.get_logged_in_user())

    def search_students(self):
        self.open_frame(self.container[1])
        self.search_student_instance.display(self.container[1])

    def view_students(self):
        self.open_frame(self.container[2])
        self.print_all_students_instance.display(self.container[2])

    def register_student(self):
        self.open_frame(self.container[3])
        self.add_student_instance.show_reg_ui(self.container[3])

    def open_frame(self, frame_open):
        
        for widget in frame_open.winfo_children():
            widget.destroy()

        for frame in self.container:
            frame.pack_forget()
        frame_open.pack(side="right", fill="both", expand=True)

    def logout_confirm(self):
        self.parent.remove_logged_in_user()
        self.parent.switch_frame('login')
