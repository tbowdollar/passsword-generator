#!/usr/bin/env python3
import Tkinter, random, string
from Tkinter import *
top = Tkinter.Tk()
top.title('Password Generator')
top.geometry('500x350')
top.resizable(width=False, height=False)
top.configure(background='#FF763A')


# Code goes here

# H1
title = Label(top, text='Password Generator', fg='#000000', bg='#FF763A', font='Helvetica 30 bold', pady=50).pack()

# Password Generation
def generate():
    pass_ = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(30))
# Password field
    pass_field = Label(top, text=pass_, fg='#000000', bg='#ff763a', font='Helvetica 15', pady=30).pack()
    
gen_button = Button(top, text='Generate', bg='#ff763a', command=generate).pack()

top.mainloop()
