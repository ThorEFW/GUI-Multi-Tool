import tkinter as tk

#   ********************* Variables

HEADLINE_FONT = ("Times",18)
LARGE_FONT = ("Times", 12)
Bg_theme = ("#1e353e")

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
        self.config(menu=mainMenu, activebackground= "green")

        fileMenu = tk.Menu(self)
        mainMenu.add_cascade(label="File", menu=fileMenu)


        self.frames = {} #This is a dictionary (i guess same as array..)

        for F in (Log_In,StartPage, RobotControl):

            frame = F (container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Log_In)

    def show_frame(self, cont):     #the "container" or "Controller" is the key whcih will look for the value of "self.frame"
                                    #   The key will specify a frame, which will be raised to the front in the "show_frame"-function
        frame = self.frames[cont]
        frame.tkraise()                 #tkraise is gonna raise the frame to the front. We can use this function because it has inherited

#def qf(string):
#    print(string)

#   *********************** StartPage Frame
#   This class will inherit from tk.frame
class Log_In(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#1e353e")

        label_Head = tk.Label(self, text="Please state your name!", font=HEADLINE_FONT, bg=Bg_theme,fg="white")
        label_Head.pack(pady=10, padx=10)
        label_intro = tk.Label(self, text="Or you want get access to this wonderful tool", font=LARGE_FONT, bg=Bg_theme, fg="white")
        label_intro.pack()

        name_label = tk.Label(self, text="Name",font=LARGE_FONT, bg=Bg_theme, fg="white")
        name_label.pack()
        name_entry = tk.Entry(self, width=25)
        name_entry.pack()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label_Head = tk.Label(self, text="Welcome to the Multi-tool!", font= HEADLINE_FONT)
        label_Head.pack(pady=10,padx=10)
        label_intro = tk.Label(self, text=" Below you will se a button where you \n can choose what ever tool you want!")
        label_intro2 = tk.Label(self, text="Amazing, i know...")

        label_intro.pack()
        label_intro2.pack()


        button_R = tk.Button(self, text="Go to Robot Control!",
                            command=lambda: controller.show_frame(RobotControl)) #By using lambda i can use the function for many things.
        button_R.pack()





class RobotControl(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
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

root = Page()
root.title('Multi-Tool')
root.geometry('{}x{}'.format(1000, 500))  # This will define the size of the window when it opens
root.mainloop()


