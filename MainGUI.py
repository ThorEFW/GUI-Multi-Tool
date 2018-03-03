from tkinter import *
import Func_GUI
import settings
import serial


root = Tk()

root.title('Robot Control Central')                                             #30px X 30px
root.geometry('{}x{}'.format(1000, 500))                                        # This will define the size of the window when it opens
root.configure(background="#1e353e")                                            # TOtal background color

#  ******* PHOTOS  *******
Robot = PhotoImage(file="Robot.png")

#***************  MENU AND SUB MENUS DECLERATION  *************
mainMenu = Menu(root, bg="blue")
root.config(menu=mainMenu)                                                      #we are configuring a menu, which is myMenu. root will look at myMenu as a menu in root window now.

fileMenu = Menu(mainMenu, bg="blue")
mainMenu.add_cascade(label="File", menu=fileMenu)                               #the Submenu, will now dropdown, when the File button is pressed
fileMenu.add_command(label="New Project...", command=Func_GUI.printingbutton)
fileMenu.add_command(label="New...", command=Func_GUI.printingbutton)
fileMenu.add_separator()
fileMenu.add_command(label="Settings", command=Func_GUI.printingbutton)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=root.quit)

editMenu = Menu(mainMenu, bg="cyan")
mainMenu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Edit something...", command=Func_GUI.printingbutton)

#************************  TOOLBAR  ***************************
toolbar = Frame(root, bg="#006100", bd=2, relief=RAISED)
Tool_label = Label(toolbar, image=Robot)
Tool_label.pack(side=LEFT, padx=2, pady=2)

toolOne = Button(toolbar,bg="white", text="Tool 1")
toolOne.pack(side=LEFT, padx=2, pady=2)
toolTwo = Button(toolbar,bg="white", text="Tool 2", command=Func_GUI.printingbutton)
toolTwo.pack(side=LEFT, padx=2, pady=2)
toolThree = Button(toolbar,bg="white", text="Tool 3", command=Func_GUI.printingbutton)
toolThree.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

#  ***********************  STATUS BAR  **************************************
statusBar = Label(root, text="Nothing", bg="#006100", bd=2, relief=SUNKEN, anchor=W) #bd=border, creates a border, relief makes it looked sunken in the screen as when a button is pressed
statusBar.pack(side=BOTTOM, fill=X)                                                 #anchor makes sure that my text appear to the left



# **************************   ALL FRAME DECLERATIONS     ****************
mid_frame = Frame(root, bg="#1e353e", width=400, height=400, padx=3, pady=3)
left_frame = Frame(root, bg="#1e353e", width=400, height=400)
right_frame = Frame(root,bg="#1e353e", width=3000, height=3000)
send_bar = Frame(root, bg="#1e353e")

# **************************  LAYOUT OF MAIN CONTAINERS ******************
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

send_bar.pack(side=TOP, fill=X)
left_frame.pack(side=LEFT,fill=BOTH)
mid_frame.pack(side=LEFT, fill=BOTH)
right_frame.pack(side=LEFT, fill=BOTH)


#   *******************  RIGHT FRAME *********************                      #create widgets for containers #width height weight sticky
Label_1 = Label(right_frame, text="Username:", padx=2, pady=2)
Label_2 = Label(right_frame, text='Password:',padx=2, pady=2)
settings.entry_1 = Entry(right_frame)
settings.entry_2 = Entry(right_frame)
check = Checkbutton(right_frame, text="COM4", command=Func_GUI.COM_4)
print_button = Button(right_frame, text="print")                                #The "command", will execute a function. Dont use "()" when calling in command


#  ******************************   SEND FRAME ********************************
settings.send_m = Button(send_bar, text="Send Message", bg="#1e73f7",fg="white", font='Times 10 bold')
settings.entry_send = Entry(send_bar, width=41)
settings.clear_button = Button(send_bar, text="Clear All", bg='#1e73f7', fg="white", font='Times 10 bold' )
settings.mid_Titel = Label(send_bar, text="Instructions Buttons", width=18, height=1, font='Times 14 bold', bg='#1e73f7', fg="white")

#   ******************************   MID-FRAME  ******************************
settings.f_forward = Button(mid_frame, text="Fast Forward",bg="#1e73f7",fg="white", font='Times 11 bold', width=21,command=Func_GUI.Fast_Forward)
settings.s_forward = Button(mid_frame, text="Slow Forward",bg="#1e73f7",fg="white", font='Times 11 bold', width=21)
settings.f_backward = Button(mid_frame, text="Fast Backward",bg="#1e73f7",fg="white", font='Times 11 bold', width=21)
settings.s_backward = Button(mid_frame, text="Slow Backward",bg="#1e73f7",fg="white", font='Times 11 bold', width=21)
settings.turn90 = Button(mid_frame, text="Turn 90 Degree",bg="#1e73f7",fg="white", font='Times 11 bold', width=21)
settings.all_stop = Button(mid_frame, text="Stop Vehicle",bg="#1e73f7",fg="white", font='Times 11 bold', width=21, command=Func_GUI.Brake)

#  *********************   BINDING FUNCTIONS TO WIDGETS   ************************
print_button.bind("<Return>", Func_GUI.printingbutton)
print_button.bind("<Button-1>", Func_GUI.printingbutton)

settings.clear_button.bind("<Button-1>", Func_GUI.clearbut)
settings.clear_button.bind("<Return>", Func_GUI.clearbut)

settings.send_m.bind("<Return>", Func_GUI.printingbutton)
settings.send_m.bind("<Button-1>", Func_GUI.printingbutton)
#top_frame.bind("<Button-1", buttonright)
#top_frame.bind("<Button-3", printrightframe)

#**********************  LEFT-FRAME LAYOUT   *************************************
settings.txt = Text(left_frame, width=50, height=20, wrap=WORD)
settings.txt.grid(row=1, column=0, pady=4, padx=4, sticky=NSEW)

# *************************    MID-FRAME LAYOUT   ***************************
settings.f_forward.grid(row=2, column=0, sticky=W, pady=4, padx=4)
settings.s_forward.grid(row=3, column=0, sticky=W, pady=4, padx=4)
settings.f_backward.grid(row=4, column=0, sticky=W, pady=4, padx=4)
settings.s_backward.grid(row=5, column=0, sticky=W, pady=4, padx=4)
settings.turn90.grid(row=6, column=0, sticky=W, pady=4, padx=4)
settings.all_stop.grid(row=7, column=0, sticky=W, pady=4, padx=4)


# *************************    RIGHT-FRAME LAYOUT   *************************
Label_1.grid(row=0, column=0)                                                   #Using grid, it don't use MID-FRAME, BUT N,S,E,W as a compass
Label_2.grid(row=1, column=0)                                                   #This will put them to the right in the grid
settings.entry_1.grid(row=0,column=1)
settings.entry_2.grid(row=1,column=1)
check.grid(row=2,columnspan=2)                                                  #The checkbox button is using 2 columns spaces ergo a span of 2
print_button.grid(row=3, column=0)


# *********************   SEND FRAME LAYOUT   *******************************
settings.send_m.grid(row=0,column=0, sticky=W, pady=2, padx=2)
settings.entry_send.grid(row=0,column=1, sticky=W, pady=2, padx=2)
settings.clear_button.grid(row=0, column=2, sticky=W,pady=2, padx=2)
settings.mid_Titel.grid(row=0, column=3, sticky=W, pady=2, padx=2)



root.mainloop()