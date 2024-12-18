import customtkinter as ctk

import ctypes

from login_frame import LoginFrame
from main_frame import MainFrame

from modules.data.data_processor import DataProcessor
from modules.student import StudentInfo

myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class App:

    SCALING = 1.5
    TITLE = "Student Management System"
    STUDENT_PATH = "app/modules/data/student_data.txt"

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    def __init__(self, data_processor: object):
        self.data_processor = data_processor
        self.data_processor.load_to_program()

        self.root = ctk.CTk()
        self.root.title(App.TITLE)
        self.root.iconbitmap('app/images/education.ico')
        self.configure_geometry()

        self.logged_in_user = None

        self.current_frame = None

        self.switch_frame('main')

    def configure_geometry(self):
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()

        root_w = int(screen_w // App.SCALING)
        root_h = int(screen_h // App.SCALING)

        root_resolution = f"{root_w}x{root_h}"

        center_x = int((screen_w - root_w) // 2)
        center_y = int((screen_h - root_h) // 2)

        geometry = f"{root_resolution}+{center_x}+{center_y}"

        self.root.geometry(geometry)

    def switch_frame(self, target_frame_name: str):
        if self.current_frame is not None:
            self.current_frame.destroy()

        if target_frame_name == "login":
            self.current_frame = LoginFrame(self)
        elif target_frame_name == "main":
            self.current_frame = MainFrame(self)
        else:
            print(f"Frame '{target_frame_name}' not found.")
            return
        self.current_frame.pack(fill="both", expand=True)


    def set_user_as_logged_in(self, user):
        self.logged_in_user = user

    def get_logged_in_user(self):
        return self.logged_in_user

    def remove_logged_in_user(self):
        self.logged_in_user = None
        print("Logged-out user removed.")

    def run(self):
        self.root.mainloop()

data_processor = DataProcessor(
    student_constructor = StudentInfo,
    data_file_path = "app/modules/data/student_data.txt"
)
app = App(
    data_processor = data_processor
)

app.run()