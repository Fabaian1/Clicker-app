from tkinter import *
from tkinter import messagebox

# Function to be called when the button is clicked
def on_button_click():
    messagebox.showinfo("Message", "You clicked the button!")

# Create a new window
window = Tk()

# Set the title of the window
window.title("My Cool App")

# Set the size of the window
window.geometry("300x200")

# Add a label to the window
label = Label(window, text="Welcome to my cool app!")
label.pack(pady=50)

# Add a button to the window
button = Button(window, text="Click me!", command=on_button_click)
button.pack()

# Run the window
window.mainloop()
