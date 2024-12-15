import customtkinter as ctk
from PIL import Image, ImageTk
from modules.log_in import LogIn

class LoginFrame(ctk.CTkFrame):
    def __init__(self, parent, students_file):
        super().__init__(parent.root, fg_color="#303030", bg_color="black")
        self.parent = parent
        self.students_file = students_file
        self.login_system = LogIn(self.students_file)

        self.create_widgets()

    def create_widgets(self):
        # Login form UI
        self.login_form = ctk.CTkFrame(self, fg_color="#303030")
        self.login_form.pack(padx=20, pady=20, expand=True)

        # Logo image (use Pillow to load the image)
        self.logo_pil = Image.open("app/images/edulogo.png")
        self.logo_pil = self.logo_pil.resize((288, 104))
        self.logo_img = ImageTk.PhotoImage(self.logo_pil)

        self.logo_label = ctk.CTkLabel(self.login_form, image=self.logo_img, text="", fg_color="#303030")
        self.logo_label.pack(pady=10)

        self.title_label = ctk.CTkLabel(self.login_form, text="Log In", text_color="white", bg_color="#303030", width=20, font=("Minercraftory", 50))
        self.title_label.pack(pady=10)

        self.id_label = ctk.CTkLabel(self.login_form, text="Enter Student ID:", text_color="white", bg_color="#303030", font=("Segoe UI", 16))
        self.id_label.pack(pady=5)

        self.id_entry = ctk.CTkEntry(self.login_form, text_color="black", bg_color="white", fg_color="#ede5e2", font=("Mojang", 16), width=250)
        self.id_entry.pack(pady=10, padx=20)

        self.error_label = ctk.CTkLabel(self.login_form, text="", bg_color="#303030", font=("Mojang", 12), text_color="red")
        self.error_label.pack(pady=5)

        # Buttons in login form
        button_frame = ctk.CTkFrame(self.login_form, fg_color="#064d2a", border_width=0)
        button_frame.pack(pady=5)

        button_frame2 = ctk.CTkFrame(self.login_form, fg_color="#0e0e0e", border_width=0)
        button_frame2.pack(pady=5)

        login_btn = ctk.CTkButton(button_frame, text="Log In", font=("Mojang", 14), fg_color="#008542", hover_color="#064d2a", width=150, height=40, command=self.login_confirm)
        exit_btn = ctk.CTkButton(button_frame2, text="Exit", font=("Mojang", 14), fg_color="#1e1e1e", hover_color="#0e0e0e", width=150, height=40, command=self.master.quit)

        login_btn.pack(padx=2, pady=2)
        exit_btn.pack(padx=2, pady=2)

    def login_confirm(self):
            studentID = self.id_entry.get().strip()
            print(f"Input ID: {studentID}")
            student = self.login_system.validate_credentials(studentID)
            if student:
                print(f"Student found: {student.get_id()}")
                self.error_label.configure(text="")
                self.id_entry.delete(0, 'end')
                self.parent.switch_frame("main")
            else:
                self.error_label.configure(text="Invalid ID. Please try again.", text_color="red")