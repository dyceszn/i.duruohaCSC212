import tkinter as tk

def say_hello():
    label.config(text="Hello, World!")

root = tk. TkO
root.title("Simple GUI")

label = tk. Label(root, text="welcome! ")
label. pack()

button = tk.Button(root, text="Greet", command=say_hello)
button.pack()

root.mainloop()