import tkinter as tk

#   ********************* Variables

LARGE_FONT = ("Times", 12)

#   ********************* Baseline! *************************
#   This allows for the functionality of changing the window/frames
class Page(tk.Tk):

    def __init__(self, *args, **kwargs):    #args = arguments, pass through variables. kwargs = keyword arguments, pass through dictionaries.

        tk.Tk.__init__(self, *args,**kwargs) # here we initialize tkinter
        container = tk.Frame(self)
        container.pack(side='top', fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {} #This is a dictionary (i guess same as array..)

        frame = StartPage(container, self)

        self.frames[StartPage] = frame

        robot_frame = RobotControl(container, self)

        self.frames[RobotControl] = robot_frame

        frame.pack()#(row=0, column=0, sticky="nsew")
        robot_frame.pack()#(row = 1, column = 0)



        self.show_frame(StartPage)

    def show_frame(self, cont):     #the "container" or "Controller" is the key whcih will look for the value of "self.frame"
                                    #   The key will specify a frame, which will be raised to the front in the "show_frame"-function
        frame = self.frames[cont]
        frame.tkraise()                 #tkraise is gonna raise the frame to the front. We can use this function because it has inherited

#   *********************** StartPage Frame
#   This class will inherit from tk.frame
class RobotControl(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="ControlPanel", font=LARGE_FONT)   #self is root
        label.pack(pady = 5 , padx = 5)

        but1 = tk.Button(self, text="Button")
        #but.grid(row=2, column=3)
        but1.pack()

        but2 = tk.Button(self, text="Button 2")
        #but.grid(row=3, column=5)
        but2.pack()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start", font= LARGE_FONT)
        label.grid(row=0, column=0)

        label1 = tk.Label(self, text=" Page , Damn", font= LARGE_FONT)
        label1.grid(row=0, column=1)

root = Page()
root.mainloop()


