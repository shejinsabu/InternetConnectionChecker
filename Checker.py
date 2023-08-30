#checking and testing URL's
from urllib import request
#GUI importation
from tkinter import *
import tkinter as tk


m = tk.Tk();
m.title('Internet Connection Checker')


out = tk.Canvas(m, width = 250, height = 150)
out.pack()

l1 = tk.Label(m, text = 'Internet Connection Checker')
l1.config(font = ('Times New Roman', 12))
out.create_window(100,25, window = l1)

l2 = tk.Label(m, text = 'Enter the URL: ')
l2.config(font = ('Times New Roman', 12))
out.create_window(100,70,window = l2)

textBox = tk.Entry(m, width = 50)
out.create_window(100,100, window = textBox)

def testingConnection():
    x = textBox.get()
    try:
        request.urlopen(x, timeout = 5)
        l3 = tk.Label(m, text = 'Congrats! The website is working!')
        l3.config(font = ('Times New Roman', 10))
        out.create_window(100,150, window = l3)
    except:
        l4 = tk.Label(m, text = 'Sorry, the website is not working')
        l4.config(font = ('Times New Roman', 10))
        out.create_window(100,150, window = l4)

button = tk.Button(m, text = 'Submit', width = 10, command = testingConnection)
button.place(x=890,y=175)

button = tk.Button(m, text='End Program', width=30, command=m.destroy)
button.place(x=825, y=300)





m.mainloop()