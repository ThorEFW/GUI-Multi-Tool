import tkinter.messagebox
import settings
import serial
import Func_GUI
from tkinter import *



#if serial.Serial("com4") != False:
#    settings.arduinoSerial = serial.Serial("com4", 9600)


# Functions for the GUI
class Controller:

    arduinoSerial = None

    def __init__(self):
        self.COM_4()


    def COM_4(self):
        if self.arduinoSerial is None:
            return self.arduinoSerial
        else:
            return self.arduinoSerial

#my_var = MyGui()


def buttonright(event):  # An event is something happening on the computer, a mouse moving, scroll, keyboard press, button on GUI, etc
    print("Right Button")


def COM_4():
    return serial.Serial("com4", 9600)




def buttonleft(event):
    print("Left button!")

    settings.arduinoSerial = COM_4()
    settings.txtPass = settings.entry_2.get()
    settings.txt.insert(0.0, str(settings.txtPass) + "\n")

    settings.txtName = settings.entry_1.get()
    settings.txt.insert(0.0, str(settings.txtName) + "\n")

def printingbutton(event):
    # answer = tkinter.messagebox.askquestion("Question Box", "what is your favorit movie?")
    settings.send_m = settings.entry_send.get()
    if str(settings.send_m) is "1":

        settings.arduinoSerial.write(b'1')

        settings.txt.insert(1000.0, "Control: " + str(settings.send_m)+ "\n", 'tag-center')
    else:
        settings.txt.insert(1000.0, "Control: " + str(settings.send_m) + "\n", 'tag-center')



def Fast_Forward():
    #settings.arduinoSerial = serial.Serial("com3", 9600)
    settings.arduinoSerial.write(b'1')
    #settings.arduinoSerial.close()
    settings.txt.insert(1000.0, "Control: Fast Forward\n", 'tag-center')

def Brake():
    #settings.arduinoSerial = serial.Serial("com3", 9600)
    settings.arduinoSerial.write(b'6')
    #settings.arduinoSerial.close()                                 #This can help in other places. Mabey when using Bluetooth
    settings.txt.insert(1000.0, "Control: Brake\n", 'tag-center')


def clearbut(event):
    settings.txt.delete(1.0, 'end')


def printrightframe(event):
    print("Right print frame")


def printleftframe(event):
    print("left print frame")



