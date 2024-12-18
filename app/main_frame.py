import os
import customtkinter as ctk
from PIL import Image, ImageTk
from modules.home import HomePage
from modules.add_student import AddStudent
from modules.search_student import Search
from modules.print_all_student import PrintAllStudents

class MainFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent.root, fg_color="white", bg_color="black")
        self.parent = parent
        self.data_processor = parent.data_processor
        
        self.container = []
        self.buttons = {}
        self.btn_txt = ["Profile", "Home", "Search Student", "View Students", "Register Student", "Log Out"]

        self.home_page_instance = HomePage()
        self.add_student_instance = AddStudent(self.data_processor)
        self.search_student_instance = Search(self.data_processor)
        self.print_all_students_instance = PrintAllStudents(self.data_processor)

        self.create_widgets()

        self.show_home()

    def create_widgets(self):        
        # Sidebar menu
        menu_container = ctk.CTkFrame(self, fg_color="#1e1e1e", bg_color="#1e1e1e", corner_radius=0)
        menu_container.pack(fill="y", side="left")

        # Topbar menu
        title_container = ctk.CTkFrame(self, fg_color="#1e1e1e", bg_color="#1e1e1e", height=90, corner_radius=0)
        title_container.pack(fill="x", side="top")

        original_image = Image.open("app/images/stu.png")
        resized_image = original_image.resize((40, 40), Image.LANCZOS)
        image_title = ImageTk.PhotoImage(resized_image)

        ctk.CTkLabel(title_container, text="Student Registration System! ", text_color="white", font=("Minercraftory", 31), image=image_title, compound="right", height=45 ).pack(anchor="w", pady=20, padx=35)

        # Content area
        self.content_frame = ctk.CTkFrame(self, fg_color="#303030", bg_color="#303030")
        self.content_frame.pack(fill="both", expand=True, side="right")


        for i in range(len(self.btn_txt) - 1):
            frame = ctk.CTkFrame(self.content_frame, fg_color="#303030")
            ctk.CTkLabel(frame, text=self.btn_txt[i], text_color="white", font=("Minercraftory", 20), width=30, anchor="center").pack(pady=20)
            self.container.append(frame)


        button_actions = [
            self.show_profile,     
            self.show_home,
            self.search_students,  
            self.view_students,    
            self.register_student, 
            self.logout_confirm    
        ]


        image_paths = [
            "app/images/profile.png",
            "app/images/home.png",
            "app/images/search.png",
            "app/images/viewall.png",
            "app/images/portal.png",
            "app/images/bed.png"
        ]
        
        self.image_refs = []

        for i, action in enumerate(button_actions):
            if not os.path.exists(image_paths[i]):
                print(f"Error: File not found - {image_paths[i]}")
                continue

            original_image = Image.open(image_paths[i])
            resized_image = original_image.resize((40, 40), Image.LANCZOS)
            image_btn = ImageTk.PhotoImage(resized_image)

            # Store image reference
            self.image_refs.append(image_btn)

            # Define custom styles for specific buttons
            if self.btn_txt[i] == "Home":
                btn_fg_color = "#1e1e1e" 
                btn_hover_color = "#303030"  
                btn_text_color = "white"
                pady_value = (4, 0)
            elif self.btn_txt[i] == "Profile":
                btn_fg_color = "#1e1e1e" 
                btn_hover_color = "#1e1e1e"  
                btn_text_color = "white"
                pady_value = (0, 0)
            elif self.btn_txt[i] == "Log Out":
                btn_fg_color = "#1e1e1e"  
                btn_hover_color = "black"  
                btn_text_color = "white"
                pady_value = (200, 0)
            else:
                btn_fg_color = "#008b45"  
                btn_hover_color = "#064d2a"  
                btn_text_color = "white"
                pady_value = (0, 0)

            # Create button
            btn = ctk.CTkButton(
                menu_container,
                text=self.btn_txt[i],
                font=("Mojang", 15),
                fg_color=btn_fg_color,
                hover_color=btn_hover_color,
                text_color=btn_text_color,
                image=image_btn,
                border_spacing=20,
                border_width=0,
                width=260,  
                height=55,  
                corner_radius=0,
                command=action,
                anchor="w"
            )
            if self.btn_txt[i] == "Log Out":
                btn.pack(pady=pady_value, side="bottom")
            else:
                btn.pack(pady=pady_value)

            self.buttons[self.btn_txt[i]] = btn

    def highlight_button(self, selected_button):
        for button_name, button in self.buttons.items():
            # Default unclicked state
            if button_name == "Home":
                button.configure(fg_color="#1e1e1e", text_color="white", hover_color="#303030")
            elif button_name == "Profile":
                button.configure(fg_color="#1e1e1e", text_color="white", hover_color="#1e1e1e")
            elif button_name == "Log Out":
                button.configure(fg_color="#1e1e1e", text_color="white", hover_color="black")
            else:  # For the last 3 buttons
                button.configure(fg_color="#008b45", text_color="white", hover_color="#064d2a")

        # Highlight the selected button
        if selected_button == self.buttons["Home"]:
            selected_button.configure(fg_color="#303030", text_color="white", hover_color="#1e1e1e")
        elif selected_button == self.buttons["Profile"]:
            selected_button.configure(fg_color="#1e1e1e", text_color="white", hover_color="#1e1e1e")
        elif selected_button == self.buttons["Log Out"]:
            selected_button.configure(fg_color="#303030", text_color="white", hover_color="#1e1e1e")
        else:  # For the last 3 buttons
            selected_button.configure(fg_color="#064d2a", text_color="white", hover_color="#303030")

    def show_profile(self):
        self.open_frame(self.container[0])
        self.add_student_instance.show_student_ui(self.container[0], self.parent.get_logged_in_user())

    def show_home(self):
        self.highlight_button(self.buttons["Home"])
        self.open_frame(self.container[1])
        self.home_page_instance.display(self.container[1])

    def search_students(self):
        self.highlight_button(self.buttons["Search Student"])
        self.open_frame(self.container[2])
        self.search_student_instance.display(self.container[2])

    def view_students(self):
        self.highlight_button(self.buttons["View Students"])
        self.open_frame(self.container[3])
        self.print_all_students_instance.display(self.container[3])

    def register_student(self):
        self.highlight_button(self.buttons["Register Student"])
        self.open_frame(self.container[4])
        self.add_student_instance.show_reg_ui(self.container[4])


    def open_frame(self, frame_open):
        '''Helper function'''
        for widget in frame_open.winfo_children():
            widget.destroy()

        for frame in self.container:
            frame.pack_forget()
        frame_open.pack(side="right", fill="both", expand=True)

    def logout_confirm(self):
        self.parent.remove_logged_in_user()
        self.parent.switch_frame('login')