import tkinter as tk
from PIL import Image, ImageTk
from tkinter import PhotoImage
from modules.log_in import LogIn
from login_window import LoginWindow
from main_window import MainWindow  # Import the MainWindow class

# ---------- MAIN WINDOW ----------
win = tk.Tk()
win.geometry("1300x800+50+50")
win.configure(bg="#000000")
win.title("Student Registration System")

icon_img = PhotoImage(file="app/images/education.png")
win.iconphoto(True, icon_img)

ctk_win = ctk.CTk()
ctk_win._root = win

students_file = "app/student_data.txt"

# ---------- CLASS INSTANCES ----------
login_system = LogIn(students_file)
login_window = LoginWindow(win, students_file)

# Create an instance of MainWindow class
main_window = MainWindow(win, students_file)

# Run the main window
win.mainloop()