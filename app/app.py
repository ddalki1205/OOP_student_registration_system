import customtkinter as ctk

from login_frame import LoginFrame
from main_frame import MainFrame

class App:

    SCALING = 1.5
    TITLE = "Student Management System"
    STUDENT_PATH = "app/modules/data/student_data.txt"

    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        self.root = ctk.CTk()
        self.root.title(App.TITLE)
        self.root.iconbitmap('app/images/education.ico')
        self.configure_geometry()

        self.logged_in_user = None

        self.current_frame = None

        self.switch_frame('login')

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
            self.current_frame = LoginFrame(self, App.STUDENT_PATH)
        elif target_frame_name == "main":
            self.current_frame = MainFrame(self, App.STUDENT_PATH)
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


app = App()
app.run()