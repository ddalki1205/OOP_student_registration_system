import customtkinter as ctk
from PIL import Image, ImageTk

class HomePage():
    def display(self, home_frame):
        frame = ctk.CTkScrollableFrame(home_frame, fg_color="#303030")
        frame.pack(expand=True, fill="both", padx=0, pady=0)

        def resize_image(event):
            my_image = Image.open("app/images/winter2.png")
            
            frame_width = event.width  
            aspect_ratio = my_image.width / my_image.height  
            new_height = int(frame_width / aspect_ratio)  

            my_image_resized = my_image.resize((frame_width, new_height))  
            
            my_image_tk = ImageTk.PhotoImage(my_image_resized)
            
            label.configure(image=my_image_tk)
            label.image = my_image_tk 

        label = ctk.CTkLabel(frame, text="")
        label.pack(expand=True, fill="both", anchor="n",  padx=0, pady=0)  

        rectangle = ctk.CTkFrame(frame, fg_color="#303030")
        rectangle.pack()
        ctk.CTkLabel(rectangle, text="Welcome to the Home Page!", font=("Minercraftory", 24), text_color="white").pack(pady=20)
        
        frame.bind("<Configure>", resize_image)