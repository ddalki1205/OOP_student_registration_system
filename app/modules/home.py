import customtkinter as ctk
from PIL import Image, ImageTk

class HomePage():
    def display(self, home_frame):
        frame = ctk.CTkScrollableFrame(home_frame, fg_color="#303030")
        frame.pack(expand=True, fill="both")

        # image
        my_image = Image.open("app/images/winter2.png")
        my_image = my_image.resize((983, 480))  
        
        my_image_tk = ImageTk.PhotoImage(my_image)
        
        label = ctk.CTkLabel(frame, image=my_image_tk, text="")
        label.pack(expand=True, fill="both")
        
        #Label
        ctk.CTkLabel(frame, text="Welcome to the Home Page!", font=("Minercraftory", 24), text_color="white").pack(pady=20)
        label.image = my_image_tk
