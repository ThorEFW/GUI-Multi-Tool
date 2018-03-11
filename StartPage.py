import tkinter as tk

#   ********************* Variables

HEADLINE_FONT = ("Times",18)
LARGE_FONT = ("Times", 12)
Bg_theme = ("#1e353e")
B_color = ("#1e73f7")
global uName


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
        fileMenu.add_command(label="Quit", command=quit)

        statusBar = tk.Label(self, text="Nothing", bg=Bg_theme, bd=2)  # bd=border, creates a border, relief makes it looked sunken in the screen as when a button is pressed
        statusBar.pack()  # anchor makes sure that my text appear to the left

        self.frames = {} #This is a dictionary (i guess same as array..)




        for F in (Log_In, StartPage, RobotControl, MovieDecider):

            frame = F (container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        #login = Log_In(container, self)
        #start_page = StartPage(container, self)
        #controll = RobotControl(container, self)


        #self.frames[Log_In] = login
        #self.frame[StartPage] = start_page
        #self.frame[RobotControl] = controll

        #controll.grid(row=0, column=0, sticky="nsew")
        #start_page.grid(row=0, column=0, sticky="nsew")
        #login.grid(row=0, column=0, sticky="nsew")



        self.show_frame(Log_In)

    def show_frame(self, cont):     #the "container" or "Controller" is the key whcih will look for the value of "self.frame"
                                    #   The key will specify a frame, which will be raised to the front in the "show_frame"-function
        frame = self.frames[cont]
        frame.tkraise()                 #tkraise is gonna raise the frame to the front. We can use this function because it has inherited



#   This class will inherit from tk.frame
class Log_In(tk.Frame):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=Bg_theme, width=400, padx=370, pady=150)

        label_Head = tk.Label(self, text="Please state your name!", font=HEADLINE_FONT, bg=Bg_theme,fg="white")
        label_Head.grid(row=0, columnspan=2)     #(side='top', expand=True)
        label_intro = tk.Label(self, text="Or you want get access to this wonderful tool", font=LARGE_FONT, bg=Bg_theme, fg="white")
        label_intro.grid(row=1, columnspan=5)        #(side='top',expand=True)

        name_label = tk.Label(self, text="Name: ",font=LARGE_FONT, bg=Bg_theme, fg="white")
        name_label.grid(row=2, column=0, sticky="w")         #(side='top',expand=True)
        name_entry = tk.Entry(self, width=25)
        name_entry.grid(row=2, column=1, sticky="w")         #(side='top',expand=True)

        pass_label = tk.Label(self, text="Password: ",font=LARGE_FONT, bg=Bg_theme, fg="white")
        pass_label.grid(row=3, column=0, sticky="w")
        pass_entry = tk.Entry(self, width=25)
        pass_entry.grid(row=3, column=1, sticky="w")

        #self.name = name_entry.get()


        log_but = tk.Button(self, text="Log In", width=16,bg=B_color, fg="white",
                            command=lambda: controller.show_frame(StartPage))
        log_but.grid(row=4, column=0, pady=7)

        q_but = tk.Button(self, text="Quit", width=16, bg=B_color, fg="white")
        q_but.grid(row=4, column=1, sticky="e")


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=Bg_theme)

        label_Head = tk.Label(self, text="Welcome to the Multi-tool!" , font= HEADLINE_FONT, bg=Bg_theme,fg="white")
        label_intro = tk.Label(self, text=" Below you will se a button where you \n can choose what ever tool you want!",bg=Bg_theme,fg="white")
        label_intro2 = tk.Label(self, text="Amazing, i know...",bg=Bg_theme,fg="white")
        label_intro3 = tk.Label(self, text="The current tools are the following: ", bg=Bg_theme, fg="white")

        label_Head.pack(pady=10, padx=10)
        label_intro.pack(pady=2)
        label_intro2.pack(pady=2)
        label_intro3.pack(pady=4)

        button_Robot = tk.Button(self, text="Robot Control", bg=B_color, fg="white",width=20, font=("Times", 14),
                                 command=lambda: controller.show_frame(RobotControl)) #By using lambda i can use the function for many things.
        button_movie = tk.Button(self, text="Movie Decider", bg=B_color, fg="white", width=20, font=("Times", 14),
                                 command=lambda: controller.show_frame(MovieDecider))
        button_Robot.pack()
        button_movie.pack()


class RobotControl(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=Bg_theme)
        label = tk.Label(self, text="ControlPanel", font=LARGE_FONT)   #self is root
        label.pack(pady=5, padx=5)

        but1 = tk.Button(self, text="Button")
        #but.grid(row=2, column=3)
        but1.pack()

        but2 = tk.Button(self, text="Button 2")
        #but.grid(row=3, column=5)
        but2.pack()

        button2 = tk.Button(self, text="Go to StartPage!",
                            command=lambda: controller.show_frame(StartPage))  # By using lambda i can use the function for many things.
        button2.pack()


class MovieDecider(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=Bg_theme)
        label = tk.Label(self, text="Movie Decider!", font=LARGE_FONT)   #self is root
        label.pack(pady=5, padx=5)


root = Page()
root.title('Multi-Tool')
width = 1000
height = 500
x = (root.winfo_screenwidth() // 2  ) - (width // 2)
y = (root.winfo_screenheight() // 2  ) - (height // 2) - 50
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))  # This will define the size of the window when it opens
root.mainloop()


