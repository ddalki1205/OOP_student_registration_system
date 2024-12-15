import customtkinter as ctk
from functools import partial
from modules.add_student import AddStudent
from modules.student import StudentInfo
from modules.search_student import Search

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

        self.create_widgets()

    def create_widgets(self):
        """
        Creates the main frame, buttons, and handles the dynamic frame creation for the sidebar menu.
        """
        # Sidebar menu
        menu_container = ctk.CTkFrame(self, fg_color="#1e1e1e", bg_color="#1e1e1e" )
        menu_container.pack(fill="y", side="left")

        # Content area
        content_frame = ctk.CTkFrame(self, fg_color="#303030", bg_color="#303030")
        content_frame.pack(fill="both", expand=True, side="right")

        # Initialize all frames dynamically
        for i in range(len(self.btn_txt) - 1):
            frame = ctk.CTkFrame(content_frame, fg_color="#303030")
            ctk.CTkLabel(frame, text=self.btn_txt[i], text_color="white", font=("Minercraftory", 30), width=30, anchor="center").pack(pady=20)
            self.container.append(frame)

        # Button functionality
        func = [partial(self.open_frame, self.container[i], self.container) for i in range(len(self.container))] + [self.logout_confirm]

        for i in range(len(self.btn_txt)):
            btn = ctk.CTkButton(menu_container, text=self.btn_txt[i], font=("Mojang", 15), fg_color="#008542", hover_color="#064d2a", width=220, height=55, command=func[i], anchor="w")
            btn.grid(row=i, column=0, pady=5)
            self.buttons.append(btn)

        # Register frame logic
        self.add_student_instance.show_reg_ui(self.container[3])
        self.search_student_instance.display(self.container[1])

    def open_frame(self, frame_open, all_frames):
        """
        Hide all frames and display the selected one.
        """
        for frame in all_frames:
            frame.pack_forget()
        frame_open.pack(side="right", fill="both", expand=True)

    def logout_confirm(self):
        """
        Log out: Clear history, reset inputs, and switch back to login screen.
        """
        for entry in self.add_student_instance.register_entry:
            entry.delete(0, 'end')
        self.parent.switch_frame('login')