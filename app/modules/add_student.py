from tkinter import *
from functools import partial

win = Tk()

win.geometry(f"{1300}x{800}+50+50")
win.config(bg="#000000")
win.title("Student Registration System")

buttons = []
container = []
btn_txt = ["View Profile", "Search Student", "Print All Students", "Register Student", "Log Out"]

def login_confirm():
    # Confirm credentials
    login_frame.pack_forget()
    main_frame.pack(fill="both", expand=True)

def logout_confirm():
    main_frame.pack_forget()
    login_frame.pack(fill="both", expand=True)

def open_frame(frame_open, all_frames):
    # Hide all frames and show the selected one
    for frame in all_frames:
        frame.pack_forget()
    frame_open.pack(side="right", fill="x")

# Login frame
login_frame = Frame(win, bg="black")
login_frame.pack(fill="both", expand=True)

login_form = Frame(login_frame, bg="white", padx=20, pady=20)
login_form.place(relx=0.5, rely=0.5, anchor="center")

Label(login_form, text="Log in", bg="skyblue", width=20, font=("Segoe UI", 18)).pack()  # Fixed label packing
login_btn = Button(login_form, text="Log In", font=("Segoe UI", 18), bg="skyblue", width=20, command=login_confirm)
exit_btn = Button(login_form, text="Exit", font=("Segoe UI", 18), bg="skyblue", width=20, command=win.quit)
login_btn.pack(pady=20)
exit_btn.pack()

# Main frame
main_frame = Frame(win, bg="white")
menu_container = Frame(main_frame, bg="green")
menu_container.pack(fill="y", side="right")
content_frame = Frame(main_frame, bg="gray")
content_frame.pack(fill="x", side="right")

# Initialize all frames
for i in range(len(btn_txt) - 1):  
    frame = Frame(content_frame, bg="pink", pady=8)
    Label(frame, text=btn_txt[i], bg="white", font=("Segoe UI", 18), width=20, anchor="center").grid(row=0, column=0, columnspan=6)
    container.append(frame)

# Button functionality
func = [
    partial(open_frame, container[i], container) for i in range(len(container))
] + [logout_confirm]

for i in range(len(btn_txt)):
    btn = Button(menu_container, bg="skyblue", font=("Segoe UI", 18), text=btn_txt[i], anchor="center", width=20, command=func[i])
    btn.grid(row=i, column=0)
    buttons.append(btn)

# Example student list and file
all_students = [] 
students_file = "../student_data.txt"  

add_student_instance = AddStudent(StudentInfo, all_students, students_file)

# Register frame logic
add_student_instance.show_reg_ui(container[2])

win.mainloop()