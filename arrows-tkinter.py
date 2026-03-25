from tkinter import *




# Build out a simple App
root = Tk()
root.title("Arrows!")
root.geometry("300x100")

def key_pressed(event):
    key = event.keysym
    print(key)
    if key == "Up":
        myLabel.config(text="UP ^")
    elif key == "Down":
        myLabel.config(text="Down v")
    elif key == "Left":
        myLabel.config(text="<-- Left")
    elif key == "Right":
        myLabel.config(text="Right -->")
    elif key == 'q':
        root.destroy()

# Label
myLabel = Label(root, text="Press arrows Keys. Press 'q' to exit....")
myLabel.pack(pady=20)


# Focus the window
root.focus_set()


# bind the keyboard
root.bind('<KeyPress>',key_pressed)


root.mainloop()