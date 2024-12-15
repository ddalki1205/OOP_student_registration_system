import tkinter as tk

root = tk.Tk()
root.title("Canvas Solid Border Example")

# Create Canvas
canvas = tk.Canvas(root, width=200, height=80, bg="white", highlightthickness=0)
canvas.pack(pady=20)

# Draw a rectangle as a border
border_color = "blue"
button_bg = "white"
button_text = "Click Me"

# Draw solid border rectangle
canvas.create_rectangle(5, 5, 195, 75, outline=border_color, width=4, fill=button_bg)

# Place text as button label
canvas.create_text(100, 40, text=button_text, font=("Arial", 14), fill="black")

root.mainloop()
