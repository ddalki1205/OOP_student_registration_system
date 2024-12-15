import customtkinter as ctk

from login_frame import LoginFrame
from main_frame import MainFrame

class App:

    SCALING = 1.7
    TITLE = "Student Management System"
    STUDENT_PATH = "app/student_data.txt"

    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        self.root = ctk.CTk()
        self.root.title(App.TITLE)
        self.root.iconbitmap('app/images/education.ico')
        self.configure_geometry()

        self.frames: dict[str : object] = {
            "login" : LoginFrame(self, App.STUDENT_PATH),
            "main" : MainFrame(self, App.STUDENT_PATH)
        }

        self.switch_frame("main")
    
    def configure_geometry(self):
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        root_w   = int(screen_w // App.SCALING)
        root_h   = int(screen_h // App.SCALING)
        center_x = int((screen_w - root_w)//2)
        center_y = int((screen_h - root_h)//2)
        root_resolution: str = f"{root_w}x{root_h}+{center_x}+{center_y}"
        self.root.geometry(root_resolution)

    def switch_frame(self, target_frame_name: str):
        for _, frame in self.frames.items():
            if frame:
                frame.pack_forget()

        frame = self.frames.get(target_frame_name)
        frame.pack(fill="both", expand=True) if frame else print("Frame not found???")
    
    def run(self):
            self.root.mainloop()

app = App()
app.run()