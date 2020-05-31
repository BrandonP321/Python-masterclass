import tkinter


def parabola(x):
    y = x ** 2 / 100
    return y


def draw_axes(canvas):
    canvas.update()
    x_origin = canvas.winfo_width() / 2  # Takes width of window and divides by 2 to find the center on x axis
    y_origin = canvas.winfo_height() / 2  # Same as x_origin but on the y axis
    canvas.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    canvas.create_line(-x_origin, 0, x_origin, 0, fill='black')
    canvas.create_line(0, y_origin, 0, -y_origin, fill='black')


def plot(canvas, x, y):
    canvas.create_line(x, y, x + 1, y + 1, fill='red')


mainWindow = tkinter.Tk()

mainWindow.geometry('640x480')
mainWindow.title('Parabola')

canvas1 = tkinter.Canvas(mainWindow, width=640, height=480)
canvas1.grid(row=0, column=0)

draw_axes(canvas1)

for x in range(-100, 101):
    y = parabola(x)
    plot(canvas1, x, -y)

mainWindow.mainloop()

# secondWindow = tkinter.Tk()
#
# secondWindow.geometry('640x480')
# secondWindow.title('Second Window')
#
# canvas2 = tkinter.Canvas(secondWindow, width=640, height=480)
# canvas2.grid(row=0, column=0)
#
# draw_axes(canvas2)
#
# for x in range(-100, 100):
#     y = x
#     canvas2.create_line(x, -y, x + 1, -y + 1, fill='black')
#
# secondWindow.mainloop()
