import tkinter as tk

def action_print():
    print('hai')

def action_exit():
    print('kthxbai')
    exit()

window = tk.Tk()
tk
button1 = tk.Button(window,text='''
AAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAA''',command=action_print)
button2 = tk.Button(window,text='''QWEQWEQWEQWEQWEQWEQWEQWE''',command=action_exit)
button1.pack()
button2.pack()
