from tkinter import *
import time

# window
root = Tk()
root.title("Watch")
root.resizable(width=False, height=False)

#func
def tick():
    watch.after(1, tick)
    watch["text"] = time.strftime("%H:%M:%S")

#watch
watch = Label(root, font="Arial 100")
watch.pack()
tick()

root.mainloop()