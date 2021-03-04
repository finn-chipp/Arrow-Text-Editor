from tkinter import *
import filedialog

#Edit these using hex values to change colour scheme
text_bg = '#36393F'
panel_bg = '#202225'
button_bg = '#36393F'
button_fg = '#FFFFFF'

def open_file():
  #this would be the insert system
  fileIn = open(browseFiles('load'), 'r')
  txt_box.delete('1.0', END)
  txt_box.insert(END, fileIn.read())

def save_file():
  #this would be the save system
  fileIn = open(browseFiles('save'), 'w')
  fileIn.write(txt_box.get("1.0","end"))
  message.set("File has been saved!")
  root.after(2500, clear_alert)

def clear_alert():
  #used to clear alerts on panel
  message.set("")

def Qsave():
  f = open(CurPath, "w")
  f.write(txt_box.get("1.0","end"))
  f.close()
  message.set("Quicksaving...")
  root.after(2500, clear_alert)

def establish():
  #just makes the settings buttons and shows S_panel
  global S_panel, FontDis, FontUp, FontDown, FontEx
  S_panel = Frame(root)
  S_panel.grid(row = 1, sticky = "n")
  S_panel['background']=panel_bg
  FontDown = Button(S_panel, bg = button_bg,activebackground=panel_bg,fg = button_fg,highlightthickness = 0,text = '-',command = lambda: rem('down'))
  FontDis = Label(S_panel, bg = button_bg,activebackground=panel_bg,fg = button_fg,highlightthickness = 0,textvariable = FontSize)
  FontUp = Button(S_panel, bg = button_bg,activebackground=panel_bg,fg = button_fg,highlightthickness = 0, text = '+',command = lambda: rem('up'))
  FontEx = Button(S_panel, bg = button_bg,activebackground=panel_bg,fg = button_fg,highlightthickness = 0,text = 'Exit',command = lambda: rem('exit'))

def rem(info):
  #gets rid of settings panel and also handles button input
  if info == 'up':
    FontSize.set(FontSize.get() + 1)
    txt_box['font'] = ("Courier", FontSize.get())
  elif info == 'down':
    FontSize.set(FontSize.get() - 1)
    txt_box['font'] = ("Courier", FontSize.get())
  else:
    S_panel.destroy()

def put():
  #*makes* and packs option buttons for S_panel
  global S_panel
  if S_panel.winfo_exists() == 0:
    establish()
  FontDis.pack(side = 'left', padx = 5, pady = 5)
  FontDown.pack(side = 'left', padx = 5, pady = 5)
  FontUp.pack(side = 'left', padx = 5, pady = 5)
  FontEx.pack(side = 'left', padx = 5, pady = 5)

def browseFiles(arg):
  global CurPath
  if arg == 'load':
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
  else:
    filename = filedialog.asksaveasfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
  CurPath = filename
  return filename

#Setting the basics up
root = Tk()
root.title("Arrow")
root.rowconfigure(0, minsize=50, weight=0)
root.columnconfigure(0, minsize=400, weight=1)
root.geometry('415x300')
message = StringVar()
FontSize = IntVar()
FontSize.set(10)
CurPath = ''

#splits the sreen into 2 sections
txt_box = Text(root, width = 25, height =  20)
panel = Frame(root, relief=RAISED, bd=2)
panel.columnconfigure(5, minsize=30, weight=1)

#___________________________________________________________
#Extraordinarily messy blob of text so it's organised
alert = Label(panel, textvariable = message, bg = panel_bg, fg = button_fg)

B_open = Button(panel, text=" Open ", command=open_file,bg = button_bg,activebackground=panel_bg,fg = button_fg,highlightthickness = 0)

B_save = Button(panel, text="Save As", command=save_file, bg = button_bg,activebackground=panel_bg,fg = button_fg,highlightthickness = 0)

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

mainloop()
