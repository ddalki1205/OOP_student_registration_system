from tkinter import *
from functools import partial
from modules.add_student import AddStudent
from modules.log_in import LogIn
from modules.print_all_student import PrintAllStudents
from modules.search_student import Search
from modules.student import StudentInfo
from modules.main_menu import MainMenu

win = Tk()

win.geometry(f"{1300}x{800}+50+50")
win.config(bg = "#000000")
win.title("Student Registration System")

buttons = [] ; container = []
btn_txt = ["View Profile", "Search Student", "Print All Students", "Register Student", "Exit"]

def login_confirm():
    #confirm creds
    login_frame.pack_forget()
    main_frame.pack(fill="both", expand=True)

def logout_confirm():
    main_frame.pack_forget()
    login_frame.pack(fill="both", expand=True)

def open_frame(frame_open, close):
    for i in range(len(close)):
        if close[i].winfo_ismapped():
            close[i].pack_forget()
    frame_open.pack(side="right", fill="x")

#login frame
login_frame = Frame(win, bg="black")
login_frame.pack(fill="both", expand=True)
login_form = Frame(login_frame, bg="white", padx=20, pady=20)
login_form.place(relx=0.5, rely=0.5, anchor="center")
Label(login_form, text="Log in", bg="skyblue", width=20, font=("Segoe UI", 18))
login_btn, exit_btn = Button(login_form, text="Log In", font=("Segoe UI", 18), bg="skyblue", width=20), Button(login_form, text="Exit", font=("Segoe UI", 18), bg="skyblue", width=20)
login_btn.pack(pady=20), exit_btn.pack()
login_btn.config(command=login_confirm)

#main frame
main_frame = Frame(win, bg="white")
menu_container = Frame(main_frame, bg="green")
menu_container.pack(fill="y", side="right")
content_frame = Frame(main_frame, bg="gray")
content_frame.pack(fill="x", side="right")


#all frames
for i in range(len(btn_txt)-1):
    container.append(Frame(content_frame, bg="pink", pady=8))
    Label(container[i], text=btn_txt[i], bg="white", font=("Segoe UI", 18), width=20, anchor="center").grid(row=0, column=0, columnspan=6)

func = [partial(open_frame, container[0], [container[1], container[2],container[3]]),
        partial(open_frame, container[1], [container[0], container[2],container[3]]),
        partial(open_frame, container[2], [container[1], container[0],container[3]]),
        partial(open_frame, container[3], [container[1], container[2],container[0]]),
        logout_confirm]

for i in range(len(btn_txt)):
    buttons.append(Button(menu_container, bg="skyblue", font=("Segoe UI", 18), text=btn_txt[i], anchor="center", width="20"))
    buttons[i].grid(row=i, column=0)
    buttons[i].config(command=func[i])

#register frame


win.mainloop()