from tkinter import *

text_bg = '#FABC45'
panel_bg = '#676543'
button_bg = '#566765'

def open_file():
  #this would be the insert system
  txt_box.delete('1.0', END)
  txt_box.insert(END, input_text)
def save_file():
  message.set("File has (not) been saved!")
  root.after(2500, clear_alert)
def clear_alert():
  message.set("")
def Qsave():
  pass

root = Tk()
root.title("Arrow Gui")
root.rowconfigure(0, minsize=50, weight=1)
root.columnconfigure(0, minsize=400, weight=1)
root.geometry('415x300')
message = StringVar()

input_text = 'qwertyuiop\nasdfghjkl\nzxcvbnm'
#Just to demonstrate, please remove

txt_box = Text(root, width = 25, height =  20)
panel = Frame(root, relief=RAISED, bd=2)
panel.columnconfigure(5, minsize=30, weight=1)

alert = Label(panel, textvariable = message, bg = panel_bg)
B_open = Button(panel, text="Open", command=open_file,bg = button_bg,highlightthickness = 0)
B_save = Button(panel, text="Save", command=save_file, bg = button_bg,highlightthickness = 0)

B_settings = Button(panel, anchor = W, text = '\u2699', font=("Courier", 20), padx = 3,bd= 0,bg = panel_bg,highlightthickness = 0)
B_qsave = Button(panel, anchor = E, text = '\u25BC', bd = 0,command = Qsave, bg = panel_bg,highlightthickness = 0)

B_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
B_save.grid(row=0, column=1, sticky="ew", padx=5)
B_settings.grid(row=0, column=6, sticky="ew", padx=5)
B_qsave.grid(row=0, column=5, sticky="ew")
alert.grid(row=0, column=2, sticky="ew", pady = 3)


panel.grid(row=0, column=0, sticky="nsew")
txt_box.grid(row=1, column=0, sticky="nsew")

txt_box['background']=text_bg
panel['background']=panel_bg

mainloop()
