from tkinter import *
from tkinter.colorchooser import *

def choose_color():
    color = askcolor()
    myLabel = Label(root, text=(color), font=("Helvetica", 16))
    myLabel.pack()

def red():
    myLabel = Label(root, text="{255.99609375 0.0 0.0} #ff0000", font=("Helvetica", 16))
    myLabel.pack()

def blue():
    myLabel = Label(root, text="{0.0 128.5 255.99609375} #0080ff", font=("Helvetica", 16))
    myLabel.pack()

def green():
    myLabel = Label(root, text="{0.0 255.99609375 0.0} #00ff00", font=("Helvetica", 16))
    myLabel.pack()

def yellow():
    myLabel = Label(root, text="{255.99609375 255.99609375 0.0} #ffff00", font=("Helvetica", 16))
    myLabel.pack()

root = Tk()
root.title('Rundom')
root.geometry("500x500")

myLabel = Label(root, text="Rundom", font=("Helvetica", 51))
myLabel.pack()
myButton = Button(root, text='Pick a color.', command=choose_color)
myButton.pack()

myLabel = Label(root, text="----Quick Color----", font=("Helvetica", 20))
myLabel.pack()
myButton = Button(root, text='Red', command=red)
myButton.pack()
myButton = Button(root, text='Blue', command=blue)
myButton.pack()
myButton = Button(root, text='Green', command=green)
myButton.pack()
myButton = Button(root, text='Yellow', command=yellow)
myButton.pack()
myLabel = Label(root, text="----------------------", font=("Helvetica", 20))
myLabel.pack()


root.mainloop()