from tkinter import *
import time

def open_file():
  #this would be the insert system
  txt_box.insert(END, input_text)
def save_file():
  alert.set("File has (not) been saved!")
  root.after(2500, clear_alert)
    
def clear_alert():
  alert.set("")

root = Tk()
root.title("Arrow Gui")
root.rowconfigure(0, minsize=50, weight=1)
root.columnconfigure(0, minsize=400, weight=1)

alert = StringVar()

input_text = 'qwertyuiop\nasdfghjkl\nzxcvbnm'
#Just to demonstrate, please remove

txt_box = Text(root)
panel = Frame(root, relief=RAISED, bd=2)
B_open = Button(panel, text="Open", command=open_file)
B_save = Button(panel, text="Save", command=save_file)
alert_msg = Label(panel, textvariable = alert).grid(row=0, column=5, sticky="ew", padx=5)

B_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
B_save.grid(row=0, column=1, sticky="ew", padx=5)

panel.grid(row=0, column=0, sticky="nsew")
txt_box.grid(row=1, column=0, sticky="nsew")

mainloop()
