import tkinter

calculator = tkinter.Tk()

calculator.title('Calculator')
calculator.geometry('640x480')
calculator['padx'] = 10

# Output field
output_entry = tkinter.Entry(calculator, relief='sunken')
output_entry.grid(row=0, column=0, columnspan=3, sticky='nescw')

# Buttons frame
buttonFrame = tkinter.Frame(calculator)
buttonFrame.grid(row=1, column=0, sticky='w')
# Buttons
# cButton = tkinter.Button(buttonFrame, text='C', relief='raised', width=5, height=2, borderwidth=3)
# ceButton = tkinter.Button(buttonFrame, text='CE', relief='raised', width=6, height=2, borderwidth=3)
# sevenButton = tkinter.Button(buttonFrame, text='7', relief='raised', borderwidth=3)
# eightButton = tkinter.Button(buttonFrame, text='8', relief='raised', borderwidth=3)
# nineButton = tkinter.Button(buttonFrame, text='9', relief='raised', width=5, height=2, borderwidth=3)
# plusButton = tkinter.Button(buttonFrame, text='+', relief='raised', width=5, height=2, borderwidth=3)
# fourButton = tkinter.Button(buttonFrame, text='4', relief='raised', height=2, borderwidth=3)
# fiveButton = tkinter.Button(buttonFrame, text='5', relief='raised', borderwidth=3)
# sixButton = tkinter.Button(buttonFrame, text='6', relief='raised', borderwidth=3)
# hyphenButton = tkinter.Button(buttonFrame, text='-', relief='raised', borderwidth=3)
# oneButton = tkinter.Button(buttonFrame, text='1', relief='raised', height=2, borderwidth=3)
# twoButton = tkinter.Button(buttonFrame, text='2', relief='raised', borderwidth=3)
# threeButton = tkinter.Button(buttonFrame, text='3', relief='raised', borderwidth=3)
# starButton = tkinter.Button(buttonFrame, text='*', relief='raised', borderwidth=3)
# zeroButton = tkinter.Button(buttonFrame, text='0', relief='raised', height=2, borderwidth=3)
# equalsButton = tkinter.Button(buttonFrame, text='=', relief='raised', borderwidth=3)
# slashButton = tkinter.Button(buttonFrame, text='/', relief='raised', borderwidth=3)

char_list = ['C', 'CE', '+', '-', '*', '=', '/']
col = 0
row = 1
for j in range(0, len(char_list)):
    if char_list[j] == 'C' or char_list[j] == "CE":
        tkinter.Button(buttonFrame, text=char_list[j], relief='raised', height=2, width=5).grid(row=0, column=col)
        col += 1
    if 1 < j < 5:
        tkinter.Button(buttonFrame, text=char_list[j], relief='raised', height=2, width=5).grid(row=row, column=3)
        row += 1
    else:
        tkinter.Button(buttonFrame, text=char_list[j], relief='raised', height=2, width=5).grid(row=4, column=(1 if char_list[j] == '=' else 3),
                                                                                                columnspan=(2 if char_list[j] == '=' else 1),
                                                                                                sticky='ew')

col = 0
for i in range(0, 10):
    if i == 0:
        tkinter.Button(buttonFrame, text=i, relief='raised', height=2, width=5).grid(row=4, column=col)
        continue
    if 1 <= i <= 3:
        tkinter.Button(buttonFrame, text=i, relief='raised', height=2, width=5).grid(row=3, column=col, sticky='nswe')
    if 4 <= i <= 6:
        tkinter.Button(buttonFrame, text=i, relief='raised', height=2, width=5).grid(row=2, column=col, sticky='nsew')
    if 7 <= i <= 9:
        tkinter.Button(buttonFrame, text=i, relief='raised', height=2, width=5).grid(row=1, column=col, sticky='nsew')
    if col < 2:
        col += 1
    else:
        col = 0

# buttons on grid
# cButton.grid(row=0, column=0, sticky='nesw')
# ceButton.grid(row=0, column=1, sticky='nesw')
# sevenButton.grid(row=1, column=0, sticky='nesw')
# eightButton.grid(row=1, column=1, sticky='ewns')
# nineButton.grid(row=1, column=2, sticky='ewns')
# plusButton.grid(row=1, column=3, sticky='ewns')
# fourButton.grid(row=2, column=0, sticky='ewns')
# fiveButton.grid(row=2, column=1, sticky='ewns')
# sixButton.grid(row=2, column=2, sticky='ewns')
# hyphenButton.grid(row=2, column=3, sticky='ewns')
# oneButton.grid(row=3, column=0, sticky='ewns')
# twoButton.grid(row=3, column=1, sticky='ewns')
# threeButton.grid(row=3, column=2, sticky='ewns')
# starButton.grid(row=3, column=3, sticky='ewns')
# zeroButton.grid(row=4, column=0, sticky='ewns')
# equalsButton.grid(row=4, column=1, columnspan=2, sticky='ewns')
# slashButton.grid(row=4, column=3, sticky='ewns')

calculator.mainloop()