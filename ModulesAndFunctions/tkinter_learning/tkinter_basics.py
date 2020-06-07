import tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

mainWindow = tkinter.Tk()
mainWindow.title("Hellow World")
mainWindow.geometry('1920x1080')

label = tkinter.Label(mainWindow, text='Hello World')
label.pack(side='top')

canvas = tkinter.Canvas(mainWindow, relief='raised', borderwidth=1)
canvas.pack(side='left')

button1 = tkinter.Button(mainWindow, text="Button 1")
button2 = tkinter.Button(mainWindow, text="Button 2")
button1.pack(side='left')
button2.pack(side='left')
mainWindow.mainloop()
