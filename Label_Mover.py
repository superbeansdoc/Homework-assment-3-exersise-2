import tkinter as tk
import random
import time

root = tk.Tk()
important_Label = tk.Label(text="cow on the sky")
y1 = important_Label.winfo_y()
x1 = important_Label.winfo_x()
def update():
    root.update()
def move_word():
    global y1
    important_Label.place(x = x1,y = y1)
    y1 = y1 + 1
    update()
    important_Label.after(1000,move_word)


important_Label.after(1000,move_word)



root.mainloop()

