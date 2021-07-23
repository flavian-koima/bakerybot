import time
import json
import os
#import tensorflow as tf
import pandas as pd
import numpy as np
from tkinter import *
from tkinter import ttk

base = Tk()
base.title('Curybot')
base.geometry('400x500')
base.resizable(width=False, height=False)

#send command
def send():
    return "Sent"

#chat history view.Immutable formatt
chathist = Text(base, bd=0, bg='white', font='Aerial')
chathist.config(state=DISABLED)

send = Button(base, font=('Aerial', 10, 'bold'), text = "Send", bg='#111000', command=send)
send.pack()


masgentry = Text(base, bg="white", fb="black")

base.mainloop()
