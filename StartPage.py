import tkinter as tk
from tkinter import ttk

#   ********************* Variables

HEADLINE_FONT = ("Times",18)
LARGE_FONT2 = ("Times", 16)
LARGE_FONT1 = ("Times", 14)
LARGE_FONT = ("Times", 12)
Bg_theme = ("#1e353e")
B_color = ("#1e73f7")
uName = ("Thor")
FG = ("white")
BC = ("#2c39b1")
#RobotImg = tk.PhotoImage(file="Robot.png")


#   ********************* Baseline! *************************
#   This allows for the functionality of changing the window/frames
class Page(tk.Tk):

    def __init__(self, *args, **kwargs):    #args = arguments, pass through variables. kwargs = keyword arguments, pass through dictionaries.

        tk.Tk.__init__(self, *args,**kwargs) # here we initialize tkinter

        container = tk.Frame(self, bg="#1e353e")
        container.pack(side='top', fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        mainMenu = tk.Menu(self)
        self.config(menu=mainMenu)

        fileMenu = tk.Menu(self)
        mainMenu.add_cascade(label="File", menu=fileMenu)
        fileMenu.add_command(label="Sign Out", command=lambda: self.show_frame(Log_In)) #This uses
        fileMenu.add_command(label="Start Page", command=lambda: self.show_frame(StartPage))
        fileMenu.add_command(label="Quit", command=quit)

        statusBar = tk.Label(self, text="Nothing", bg=Bg_theme, bd=3,fg="white", relief="sunken", anchor="w")  # bd=border, creates a border, relief makes it looked sunken in the screen as when a button is pressed
        statusBar.pack(side="bottom", fill="x")  # anchor makes sure that my text appear to the left

        self.frames = {} #This is a dictionary (i guess same as array..)

        #for F in (Log_In, StartPage, RobotControl, MovieDecider):
        #    frame = F (container, self)
        #    self.frames[F] = frame
        #    frame.grid(row=0, column=0, sticky="nsew")

        controll = RobotControl(container, self)
        start_page = StartPage(container, self, controll)
        login = Log_In(container, self, start_page,)



        self.frames[Log_In] = login
        self.frames[StartPage] = start_page
        self.frames[RobotControl] = controll

        controll.grid(row=0, column=0, sticky="nsew")
        start_page.grid(row=0, column=0, sticky="nsew")
        login.grid(row=0, column=0, sticky="nsew")



        self.show_frame(Log_In)

    def show_frame(self, cont):     #the "container" or "Controller" is the key whcih will look for the value of "self.frame"
                                    #   The key will specify a frame, which will be raised to the front in the "show_frame"-function
        frame = self.frames[cont]
        frame.tkraise()                 #tkraise is gonna raise the frame to the front. We can use this function because it has inherited



#   This class will inherit from tk.frame
class Log_In(tk.Frame):

    def __init__(self, parent, controller, start_page):
        self.start_page = start_page
        tk.Frame.__init__(self, parent)#, bg=Bg_theme, width=400, padx=370, pady=150)
        self.Universe = tk.PhotoImage(file="Pics/Universe.png")

        self.PhotoLabel = tk.Label(self, image=self.Universe)
        self.PhotoLabel.place(x=0, y=0, relwidth=1, relheight=1)

        main_frame = tk.Frame(self, bg=Bg_theme)  # bg
        main_frame.place(relx=0.5, rely=0.5, anchor="center")

        label_Head = tk.Label(main_frame, text="Please state your name!", font=HEADLINE_FONT, bg=Bg_theme,fg="white")
        label_Head.grid(row=0, columnspan=2)     #(side='top', expand=True)
        label_intro = tk.Label(main_frame, text="Or you want get access to this wonderful tool", font=LARGE_FONT, bg=Bg_theme, fg="white")
        label_intro.grid(row=1, columnspan=5)        #(side='top',expand=True)

        name_label = tk.Label(main_frame, text="Name: ",font=LARGE_FONT, bg=Bg_theme, fg="white")
        name_label.grid(row=2, column=0, sticky="w")         #(side='top',expand=True)
        name_entry = tk.Entry(main_frame,width=25)
        name_entry.grid(row=2, column=1, sticky="w")         #(side='top',expand=True)

        pass_label = tk.Label(main_frame, text="Password: ",font=LARGE_FONT, bg=Bg_theme, fg="white")
        pass_label.grid(row=3, column=0, sticky="w")
        pass_entry = tk.Entry(main_frame,show="*", width=25)
        pass_entry.grid(row=3, column=1, sticky="w")


        #log_but = tk.Button(self, text="Log In", width=16,
        #                     command=lambda: controller.show_frame(StartPage))
        log_but = tk.Button(main_frame, text="Log In", width=16, bg=B_color,fg="white",
                            command=lambda: self.start_page.setName_S(name_entry.get(), pass_entry.get()))
        log_but.grid(row=4, column=0, pady=7)
       # log_but.bind("<Button-1>", lambda: controller.show_frame(StartPage))

        q_but = tk.Button(main_frame, text="Quit", width=16, bg=B_color, fg="white")
        q_but.grid(row=4, column=1, sticky="e")


class StartPage(tk.Frame):

    def __init__(self, parent, controller, controll):
        global name
        self.uname = None
        self.passW = None
        self.controll = controll
        tk.Frame.__init__(self, parent, bg=Bg_theme)
        self.controller = controller

        self.Universe = tk.PhotoImage(file="Pics/Universe.png")
        self.PhotoLabel = tk.Label(self, image=self.Universe)
        self.PhotoLabel.place(x=0, y=0, relwidth=1, relheight=1)

        self.label_Head = tk.Label(self, font=HEADLINE_FONT,
                                   bg=Bg_theme, fg="white")
        self.label_pass = tk.Label(self, bg=Bg_theme, fg=FG)
        label_intro = tk.Label(self,
                               text=" Below you will se a button where you \n can choose what ever tool you want!",
                               bg=Bg_theme, fg="white")
        label_intro2 = tk.Label(self, text="Amazing, i know...", bg=Bg_theme, fg="white")
        label_intro3 = tk.Label(self, text="The current tools are the following: ", bg=Bg_theme, fg="white")

        self.label_Head.pack(pady=10, padx=10)
        self.label_pass.pack(pady=10, padx=10)
        label_intro.pack(pady=2)
        label_intro2.pack(pady=2)
        label_intro3.pack(pady=4)

        #button_Robot = tk.Button(self, text="Robot Control", bg=B_color, fg="white", width=20, font=("Times", 14),
        #                        command=lambda: self.controller.show_frame(RobotControl))  # By using lambda i can use the function for many things.
        button_Robot = tk.Button(self, text="Robot Control", bg=B_color, fg="white", width=20, font=("Times", 14),
                                 command=lambda: self.controll.setName_C(self.setName_S))

        button_movie = tk.Button(self, text="Movie Decider", bg=B_color, fg="white", width=20, font=("Times", 14),
                                 command=lambda: self.controller.show_frame(MovieDecider))
        button_Robot.pack()
        button_movie.pack()

    def setName_S(self, name, passW):
        self.uname = name
        self.passW = passW
        if name != None:
            self.label_Head.configure(text = "Welcome to the Multi-tool " + self.uname + "!")
        if passW != None:
            self.label_pass.configure(text="Your password is '"+self.passW+ "', hehe")
        else:
            self.label_pass.configure(text="You did not enter a password..")
        self.tkraise()
        return name


class RobotControl(tk.Frame):
    i = None
    def __init__(self, parent, controller):
        self.name = None
        self.passW = None

        tk.Frame.__init__(self, parent, bg=Bg_theme)

        self.Universe = tk.PhotoImage(file="Pics/Universe.png")

        self.PhotoLabel = tk.Label(self, image=self.Universe)
        self.PhotoLabel.place(x=0, y=0, relwidth=1, relheight=1)

        self.txtOut  = ""
        self.RobotImg = tk.PhotoImage(file="Pics/Robot.png")
        self.WALLE = tk.PhotoImage(file="Pics/Walle.png")
    # --------------------------------------------------    Top
        #HeadLineFrame = tk.Frame(self, bg=Bg_theme)
        #HeadLineFrame.pack(side="top", fill="x")

        H_line = tk.Label(self, text="Robot Control Center", font=HEADLINE_FONT, bg=Bg_theme, fg="white")
        self.fil_lab = tk.Label(self, text="__________", bg=Bg_theme, fg=Bg_theme, width=23)
        self.but_instruct = tk.Label(self, text="Instruction Buttons", bg=Bg_theme, fg="white", font=LARGE_FONT2)

        H_line.grid(row=0, columnspan=2)
        self.but_instruct.grid(row=0, column=3)

        #Head_Img = tk.Label(HeadLineFrame, image=RobotImg)
        #Head_Img.grid(row=0, column=0)

    # ----------------------------------------------------  Left
        #left_frame = tk.Frame(self, bg=Bg_theme)
        #left_frame.pack(side="left", fill="y")

        self.but_send = tk.Button(self, text="Send", width=5, bg=BC, fg=FG)
        self.mes_entry = tk.Entry(self, width=40)
        self.clear_but = tk.Button(self, text="Delete text", width=10, bg=BC, fg=FG)
        self.txt_field = tk.Text(self, width=25, height=22, wrap="word", yscrollcommand=set(), borderwidth=5, padx=3, font="systemfixed")
        self.F_forward = tk.Button(self, text="Fast Forward", width=25, bg=BC, fg=FG)
        self.S_forward = tk.Button(self, text="Slow Forward", width=25, bg=BC, fg=FG)
        self.F_backward = tk.Button(self, text="Fast Backward", width=25, bg=BC, fg=FG)
        self.S_backward = tk.Button(self, text="Slow Backward", width=25, bg=BC, fg=FG)
        self.R_turn = tk.Button(self, text="Right Turn", width=25, bg=BC, fg=FG)
        self.L_turn = tk.Button(self, text="Left Turn", width=25, bg=BC, fg=FG)
        self.All_stop = tk.Button(self, text="Motor Stop", width=25, bg=BC, fg=FG)
        self.bind_spot = tk.Button(self, text="Push this button to \n control with W,A,S,D. \n Yellow = Active", width=25, height=5, bg=BC, fg=FG)

        self.but_send.grid(row=1, column=0, pady=3, padx=2)
        self.mes_entry.grid(row=1, column=1, pady=3, padx=2)
        self.clear_but.grid(row=1, column=2, pady=3, padx=2)
        self.txt_field.grid(rowspan=10, columnspan=3, pady=3, padx=2, sticky="nsew")
        self.F_forward.grid(row=2,column=3, padx=20,pady=5, sticky="n")
        self.S_forward.grid(row=3,column=3, padx=20,pady=5, sticky="n")
        self.F_backward.grid(row=4,column=3, padx=20,pady=5, sticky="n")
        self.S_backward.grid(row=5,column=3, padx=20,pady=5, sticky="n")
        self.R_turn.grid(row=6,column=3, padx=20,pady=5, sticky="n")
        self.L_turn.grid(row=7,column=3, padx=20,pady=5, sticky="n")
        self.All_stop.grid(row=8,column=3, padx=20,pady=5, sticky="n")
        self.bind_spot.grid(row=9, column=3,padx=20, pady=15, sticky="n")

        self.but_send.bind("<Button-1>", self.printing)
        self.clear_but.bind("<Button-1>", self.clear)
        self.F_forward.bind("<Button-1>", self.forward)
        self.S_forward.bind("<Button-1>", self.forward)
        self.F_backward.bind("<Button-1>", self.backward)
        self.S_backward.bind("<Button-1>", self.backward)
        self.R_turn.bind("<Button-1>", self.right_turn)
        self.L_turn.bind("<Button-1>", self.left_turn)
        self.All_stop.bind("<Button-1>", self.Stop)

        self.bind_spot.bind("<w>", self.forward)
        self.bind_spot.bind("<s>", self.backward)
        self.bind_spot.bind("<a>", self.left_turn)
        self.bind_spot.bind("<d>", self.right_turn)
        self.bind_spot.bind("<x>", self.Stop)
        self.bind_spot.bind("<Button-1>", self.Button_color)

        self.PhotoLabel = tk.Label(self, image=self.WALLE)
        self.PhotoLabel.grid(row=2, rowspan=8, column=4)

    def setName_C(self, name):
        self.tkraise()

    def printing(self, event):      # Include "name" then the username should be included.. later
        #self.name = name
        print("hey")
        self.txtOut = self.mes_entry.get()
        self.txt_field.insert(1000000.0, "Controller:" + str(self.txtOut) + "\n")
        self.mes_entry.delete(0, 'end')

    def forward(self, event):
        print("Forward")
        self.txt_field.insert(100000.0,"Controller: Forward\n")

    def backward(self, event):
        print("Backward")
        self.txt_field.insert(100000.0, "Controller: Backward\n")

    def left_turn(self, event):
        print("Left Turn")
        self.txt_field.insert(1000000.0, "Controller: Left Turn\n")

    def right_turn(self, event):
        print("Right Turn")
        self.txt_field.insert(1000000.0, "Controller: Right Turn\n")

    def Stop(self, event):
        print("Stop")
        self.txt_field.insert(10000.0, "Controller: Stop\n")

    def clear(self, event):
        self.txt_field.delete(1.0, 'end')

    def Button_color(self, event):

        if self.i is None:
            self.bind_spot.configure(bg="yellow", fg="black")
            self.bind_spot.focus_set()
            self.i = 1
        else:
            self.bind_spot.configure(bg="#2c39b1", fg=FG)
            self.but_send.focus_set()
            self.i = None

class MovieDecider(tk.Frame):

    def __init__(self, parent, controller):
        self.PopCorn = tk.PhotoImage(file="Pics/Popcorn.png")

        tk.Frame.__init__(self, parent, bg=Bg_theme)
        label = ttk.Label(self, text="Movie Decider!", font=LARGE_FONT)   #self is root
        label.pack(pady=5, padx=5)


root = Page()
root.title('Multi-Tool')
width = 1050
height = 575
x = (root.winfo_screenwidth() // 2  ) - (width // 2)
y = (root.winfo_screenheight() // 2  ) - (height // 2) - 50
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))  # This will define the size of the window when it opens
root.mainloop()


