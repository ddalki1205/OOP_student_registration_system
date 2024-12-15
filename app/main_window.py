import customtkinter as ctk
from functools import partial
from modules.add_student import AddStudent
from modules.student import StudentInfo

class MainWindow:
    def __init__(self, win, students_file):
        self.win = win
        self.students_file = students_file
        self.main_frame = ctk.CTkFrame(self.win, fg_color="white", bg_color="#303030")
        self.container = []
        self.buttons = []
        self.btn_txt = ["View Profile", "Search Student", "Print All Students", "Register Student", "Log Out"]
        
        # Create the add student instance
        self.add_student_instance = AddStudent(StudentInfo, self.students_file)

        self.create_widgets()

    def create_widgets(self):
        """
        Creates the main frame, buttons, and handles the dynamic frame creation for the sidebar menu.
        """
        # Sidebar menu
        menu_container = ctk.CTkFrame(self.main_frame, fg_color="#1e1e1e")
        menu_container.pack(fill="y", side="left")

        # Content area
        content_frame = ctk.CTkFrame(self.main_frame, fg_color="#303030")
        content_frame.pack(fill="both", expand=True, side="right")

        # Initialize all frames dynamically
        for i in range(len(self.btn_txt) - 1):
            frame = ctk.CTkFrame(content_frame, fg_color="lightgray")
            ctk.CTkLabel(frame, text=self.btn_txt[i], text_color="white", font=("Segoe UI", 18), width=30, anchor="center").pack(pady=20)
            self.container.append(frame)

        # Button functionality
        func = [partial(self.open_frame, self.container[i], self.container) for i in range(len(self.container))] + [self.logout_confirm]

        for i in range(len(self.btn_txt)):
            btn = ctk.CTkButton(menu_container, text=self.btn_txt[i], font=("Segoe UI", 18), fg_color="skyblue", width=200, command=func[i])
            btn.grid(row=i, column=0, pady=5)
            self.buttons.append(btn)

        # Register frame logic
        self.add_student_instance.show_reg_ui(self.container[3])

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
        # Reset entries and clear error labels
        for entry in self.add_student_instance.register_entry:
            entry.delete(0, 'end')

        self.main_frame.pack_forget()  # Hide the main interface
        self.container[0].pack(fill="both", expand=True)  # Show the login frame