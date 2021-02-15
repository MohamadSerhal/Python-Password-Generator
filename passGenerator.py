import tkinter as tk
from tkinter import ttk
from tkinter import *
import random

lowerCase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upperCase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'k', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!', '@', '#', '$', '%', '&']

def generatePass(x, y, z, size):
    sizeLeft = size
    groupsAvailable = []
    groupsAvailable.append(lowerCase)
    passW = ""
    if x:
        groupsAvailable.append(upperCase)
    if y:
        groupsAvailable.append(numbers)
    if z:
        groupsAvailable.append(symbols)
    while sizeLeft>0:
        x = random.choice(groupsAvailable)
        kind2 = random.choice(x)
        passW = passW + kind2
        sizeLeft = sizeLeft -1
    return passW


root = Tk()
#this is the declaration of the variable associated with the checkbox
checkCapitalLetters = tk.IntVar()
#this is the declaration of the variable associated with the checkbox
checkSymbols = tk.IntVar()
#this is the declaration of the variable associated with the checkbox
checkNumbers = tk.IntVar()

# This is the section of code which creates the main window
root.geometry('650x400')
root.configure(background='#F5F5DC')
root.title('Password Generator')

# This is the section of code which creates the a label
Label(root, text='Password Generator', bg='#F5F5DC', font=('arial', 16, 'normal')).place(x=238, y=14)

# This is the section of code which creates the a label
Label(root, text='This password generator, creates passwords depending on user preferences!', bg='#F5F5DC', font=('arial', 12, 'normal')).place(x=24, y=60)

# This is the section of code which creates a checkbox
capitalLettersCheckBox=Checkbutton(root, text='capital letters', variable=checkCapitalLetters, bg='#F5F5DC', font=('arial', 12, 'normal'))
capitalLettersCheckBox.place(x=173, y=100)

# This is the section of code which creates a checkbox
symbolsCheckBox=Checkbutton(root, text='symbols', variable=checkSymbols, bg='#F5F5DC', font=('arial', 12, 'normal'))
symbolsCheckBox.place(x=188, y=150)

# This is the section of code which creates a checkbox
numbersCheckBox=Checkbutton(root, text='numbers', variable=checkNumbers, bg='#F5F5DC', font=('arial', 12, 'normal'))
numbersCheckBox.place(x=186, y=200)

# This is the section of code which creates a spin box
spinBoxSize= Spinbox(root, from_=8, to=24, font=('arial', 12, 'normal'), bg = '#F5F5DC', width=10)
spinBoxSize.place(x=176, y=250)

# This is the section of code which creates the a label
Label(root, text='Password Size:', bg='#F5F5DC', font=('arial', 12, 'normal')).place(x=46, y=250)

# This is the section of code which creates the a label
Label(root, text='Your Password:', bg='#F5F5DC', font=('arial', 12, 'normal')).place(x=40, y=300)

# This is the section of code which creates the a label
answerVar = StringVar()
answerVar.set("")
answertext=Entry(root, state='readonly', textvariable=answerVar, width=30, font=('arial', 12, 'normal'))
answertext.place(x=170, y=300)

# This is the section of code which creates the a label
errorVar = StringVar()
errorVar.set("")
Label(root, textvariable=errorVar, bg='#F5F5DC', fg='red', font=('arial', 12, 'normal')).place(x=40, y=350)

# this is the function called when the button is clicked
def btnClickFunction():
    capLetters = checkCapitalLetters.get()
    numbs = checkNumbers.get()
    symbs = checkSymbols.get()
    size = int(spinBoxSize.get())
    if size<8:
        errorVar.set("NOTICE: your password is weak, it has less than 8 characters!")
    ans  = generatePass( capLetters, numbs, symbs, size)
    answerVar.set(ans)

# This is the section of code which creates a button
Button(root, text='Generate!', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction).place(x=450, y=144)


root.mainloop()
