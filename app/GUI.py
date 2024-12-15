from tkinter import *
from functools import partial
from modules.log_in import LogIn
from modules.add_student import AddStudent
from modules.student import StudentInfo

# ---------- MAIN WINDOW ----------
win = Tk()
win.geometry("1300x800+50+50")
win.config(bg="#000000")
win.title("Student Registration System")

buttons = []
container = []
btn_txt = ["View Profile", "Search Student", "Print All Students", "Register Student", "Log Out"]

# Simulated student database
all_students = []
students_file = "student_data.txt"

# ---------- CLASS INSTANCES ----------
login_system = LogIn()
add_student_instance = AddStudent(StudentInfo, all_students, students_file)

# ---------- FUNCTION DEFINITIONS ----------
def login_confirm():
    """
    Confirm credentials: switch from login to main interface.
    """
    studentID = id_entry.get()  # Get input from entry field
    student = login_system.validate_credentials(all_students, studentID)
    
    if student:
        error_label.config(text="Login Successful!", fg="green")
        login_frame.pack_forget()
        main_frame.pack(fill="both", expand=True)
    else:
        if login_system.remaining_attempts() > 0:
            error_label.config(text=f"Invalid ID. {login_system.remaining_attempts()} attempts left.", fg="red")
        else:
            error_label.config(text="Too many failed attempts. Exiting...", fg="red")
            win.quit()

def logout_confirm():
    """
    Log out: switch back to login screen.
    """
    main_frame.pack_forget()
    login_frame.pack(fill="both", expand=True)

def open_frame(frame_open, all_frames):
    """
    Hide all frames and show the selected one.
    """
    for frame in all_frames:
        frame.pack_forget()
    frame_open.pack(side="right", fill="both", expand=True)

# ---------- LOGIN FRAME ----------
login_frame = Frame(win, bg="black")
login_frame.pack(fill="both", expand=True)

# Login form UI
login_form = Frame(login_frame, bg="white", padx=20, pady=20)
login_form.place(relx=0.5, rely=0.5, anchor="center")

Label(login_form, text="Log In", bg="skyblue", width=20, font=("Segoe UI", 18)).pack(pady=10)
Label(login_form, text="Enter Student ID:", font=("Segoe UI", 14)).pack(pady=5)

id_entry = Entry(login_form, font=("Segoe UI", 14), width=20)
id_entry.pack(pady=5)

error_label = Label(login_form, text="", font=("Segoe UI", 12), fg="red")
error_label.pack(pady=5)

login_btn = Button(login_form, text="Log In", font=("Segoe UI", 18), bg="skyblue", width=20, command=login_confirm)
exit_btn = Button(login_form, text="Exit", font=("Segoe UI", 18), bg="skyblue", width=20, command=win.quit)

login_btn.pack(pady=10)
exit_btn.pack()

# ---------- MAIN INTERFACE ----------
main_frame = Frame(win, bg="white")

# Sidebar menu
menu_container = Frame(main_frame, bg="green")
menu_container.pack(fill="y", side="left")

# Content area
content_frame = Frame(main_frame, bg="gray")
content_frame.pack(fill="both", expand=True, side="right")

# Initialize all frames
for i in range(len(btn_txt) - 1):  
    frame = Frame(content_frame, bg="pink", pady=8)
    Label(frame, text=btn_txt[i], bg="white", font=("Segoe UI", 18), width=20, anchor="center").pack()
    container.append(frame)

# Button functionality
func = [
    partial(open_frame, container[i], container) for i in range(len(container))
] + [logout_confirm]

for i in range(len(btn_txt)):
    btn = Button(menu_container, bg="skyblue", font=("Segoe UI", 18), text=btn_txt[i], anchor="center", width=20, command=func[i])
    btn.grid(row=i, column=0)
    buttons.append(btn)

# Register frame logic
add_student_instance.show_reg_ui(container[2])  # Load "Register Student" frame

# ---------- RUN MAINLOOP ----------
win.mainloop()