import customtkinter as ctk
from PIL import Image, ImageTk

class LoginFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent.root, fg_color="#303030", bg_color="black")
        self.parent = parent

        self.create_widgets()

    def create_widgets(self):
        # Login form UI
        self.login_form = ctk.CTkFrame(self, fg_color="#303030", corner_radius=0)
        self.login_form.pack(pady=80)

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
        button_frame = ctk.CTkFrame(self.login_form, fg_color="#303030", border_width=190)
        button_frame.pack(pady=10)

        login_btn = ctk.CTkButton(button_frame, text="Log In", font=("Mojang", 14), fg_color="#008542", hover_color="#064d2a", width=180, height=40, 
                                  corner_radius=0, border_spacing=15, command=self.login_confirm)
        exit_btn = ctk.CTkButton(button_frame, text="Exit", font=("Mojang", 14), fg_color="#1e1e1e", hover_color="#0e0e0e", width=180, height=40, 
                                 corner_radius=0, border_spacing=15, command=self.master.quit)

        login_btn.pack(padx=2, pady=7)
        exit_btn.pack(padx=2, pady=7)

    def login_confirm(self):
            student_id = self.id_entry.get().strip()
            student = self.parent.data_processor.fetch_student_by_id(student_id)
            if student:
                self.error_label.configure(text="")
                self.id_entry.delete(0, 'end')
                self.parent.set_user_as_logged_in(student)
                self.parent.switch_frame("main")
            else:
                self.error_label.configure(text="Invalid ID.\n\nPlease try again.", text_color="red")