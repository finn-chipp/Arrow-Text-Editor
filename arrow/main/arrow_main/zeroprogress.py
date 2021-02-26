from tkinter import *

#Edit these using hex values to change colour scheme
text_bg = '#36393F'
panel_bg = '#202225'
button_bg = '#36393F'
button_fg = '#FFFFFF'

def open_file():
  #this would be the insert system
  txt_box.delete('1.0', END)
  txt_box.insert(END, input_text)

def save_file():
  #this would be the save system
  message.set("File has (not) been saved!")
  root.after(2500, clear_alert)

def clear_alert():
  #used to clear alerts on panel
  message.set("")

def Qsave():
  #Quick save to be added
  pass

def establish():
  #just makes the settings buttons and shows S_panel
  global S_panel, O_font, O_cct, O_ccl
  S_panel = Frame(root)
  S_panel.grid(row = 1, sticky = "n")
  S_panel['background']=panel_bg
  O_font = Button(S_panel, bg = button_bg,activebackground=panel_bg,fg = button_fg,highlightthickness = 0,text = 'Font',command = lambda: rem('opt1'))
  O_cct = Button(S_panel, bg = button_bg,activebackground=panel_bg,fg = button_fg,highlightthickness = 0,text = 'CC Toggle',command = lambda: rem('opt2'))
  O_ccl = Button(S_panel, bg = button_bg,activebackground=panel_bg,fg = button_fg,highlightthickness = 0, text = 'CC List',command = lambda: rem('opt3'))

def rem(info):
  #gets rid of settings panel and also handles button input
  S_panel.destroy()
  if info == 'opt1':
    print('1')
  elif info == 'opt2':
    print('2')
  else:
    print('3')

def put():
  #*makes* and packs option buttons for S_panel
  global S_panel
  if S_panel.winfo_exists() == 0:
    establish()
  O_font.pack(side = 'left', padx = 5, pady = 5)
  O_cct.pack(side = 'left', padx = 5, pady = 5)
  O_ccl.pack(side = 'left', padx = 5, pady = 5)

#Setting the basics up
root = Tk()
root.title("Arrow Gui")
root.rowconfigure(0, minsize=50, weight=0)
root.columnconfigure(0, minsize=400, weight=1)
root.geometry('415x300')
message = StringVar()

#------
input_text = 'qwertyuiop\nasdfghjkl\nzxcvbnm'
#Just to demonstrate, please remove
#------

#splits the sreen into 2 sections
txt_box = Text(root, width = 25, height =  20)
panel = Frame(root, relief=RAISED, bd=2)
panel.columnconfigure(5, minsize=30, weight=1)

#___________________________________________________________
#Extraordinarily messy blob of text so it's organised
alert = Label(panel, textvariable = message, bg = panel_bg)

B_open = Button(panel, text="Open", command=open_file,bg = button_bg,activebackground=panel_bg,fg = button_fg,highlightthickness = 0)

B_save = Button(panel, text="Save", command=save_file, bg = button_bg,activebackground=panel_bg,fg = button_fg,highlightthickness = 0)

B_settings = Button(panel, anchor = W, text = '\u2699', font=("Courier", 20), padx = 3,bd= 0,bg = panel_bg,fg = button_fg,activebackground=panel_bg,highlightthickness = 0, command = put)

B_qsave = Button(panel, anchor = E, text = '\u25BC', bd = 0,command = Qsave, bg = panel_bg,fg = button_fg,activebackground=panel_bg,highlightthickness = 0)

B_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
B_save.grid(row=0, column=1, sticky="ew", padx=5)
B_settings.grid(row=0, column=6, sticky="ew", padx=5)
B_qsave.grid(row=0, column=5, sticky="ew")
alert.grid(row=0, column=2, sticky="ew", pady = 3)
#‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
establish()

panel.grid(row=0, column=0, sticky="nsew")
txt_box.grid(row=1, column=0, sticky="nsew")

#Just some touching up
txt_box['background']=text_bg
txt_box['foreground']=button_fg
panel['background']=panel_bg

photo = PhotoImage(file = "'arrow_icon.png")
master.iconphoto(False, photo)

mainloop()
