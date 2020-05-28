import tkinter
import os

mainWindow = tkinter.Tk()

mainWindow.title("Grid Demo")
mainWindow.geometry("640x480")

label = tkinter.Label(mainWindow, text="Tkinter Grid Demo")
label.grid(row=0, column=0, columnspan=3)

mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=3)
mainWindow.columnconfigure(3, weight=3)
mainWindow.columnconfigure(4, weight=3)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)
mainWindow.rowconfigure(4, weight=3)

# file list box
fileList = tkinter.Listbox(mainWindow)
fileList.grid(row=1, column=0, rowspan=2, sticky='nesw')
fileList.config(border=2, relief='sunken')
for zone in os.listdir('C:\Windows\System32'):
    fileList.insert(tkinter.END, zone)

# scroll bar for list
listScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, comman=fileList.yview)
listScroll.grid(row=1, column=1, rowspan=2, sticky='nsw')
fileList['yscrollcommand'] = listScroll.set

# Frame for radio buttons
optionFrame = tkinter.LabelFrame(mainWindow, text='File Details')
optionFrame.grid(row=1, column=2, sticky='ne')

rbValue = tkinter.IntVar()
rbValue.set(3)

# radio buttons
radio1 = tkinter.Radiobutton(optionFrame, text='File name', value=1, variable=rbValue)
radio2 = tkinter.Radiobutton(optionFrame, text='Path', value=2, variable=rbValue)
radio3 = tkinter.Radiobutton(optionFrame, text='Timestamp', value=3, variable=rbValue)
radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')

# result label and entry
resultLabel = tkinter.Label(mainWindow, text='Result')
resultLabel.grid(row=2, column=2, sticky='nw')
result = tkinter.Entry(mainWindow)
result.grid(row=2, column=2, sticky='sw')

# create frame for time
timeFrame = tkinter.LabelFrame(mainWindow, text='Time')
timeFrame.grid(row=3, column=0, sticky='new')
# create spinners and place on grid
hourSpinner = tkinter.Spinbox(timeFrame, width=2, values=tuple(range(0, 24)))
minuteSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
secondSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
hourSpinner.grid(row=0, column=0)
tkinter.Label(timeFrame, text=':').grid(row=0, column=1)
minuteSpinner.grid(row=0, column=2)
tkinter.Label(timeFrame, text=':').grid(row=0, column=3)
secondSpinner.grid(row=0, column=4)
# add padding to left and right of contents of timeFrame
timeFrame['padx'] = 36

# frame for date
dateFrame = tkinter.Frame(mainWindow)
dateFrame.grid(row=4, column=0, sticky='new')

# labels for date
dayLabel = tkinter.Label(dateFrame, text='Day',)
monthLabel = tkinter.Label(dateFrame, text='Month')
yearLabel = tkinter.Label(dateFrame, text='Year')
dayLabel.grid(row=0, column=0, sticky='w')
monthLabel.grid(row=0, column=1, sticky='w')
yearLabel.grid(row=0, column=2, sticky='w')

# date spinners
daySpinner = tkinter.Spinbox(dateFrame, width=5, from_=1, to=31)
daySpinner.grid(row=1, column=0, sticky='w')
monthSpinner =tkinter.Spinbox(dateFrame, width=5, values=('Jan', 'Feb', "Mar", "Apr", "May", "Jun", "Jul",
                                                          "Aug", "Sep", "Oct", "Nov", "Dec"))
monthSpinner.grid(row=1, column=1, sticky='w')
yearSpinner = tkinter.Spinbox(dateFrame, width=5, from_=2000, to=2099)
yearSpinner.grid(row=1, column=2, sticky='w')

# padding dateFrame
dateFrame['padx'] = 20


mainWindow.mainloop()
