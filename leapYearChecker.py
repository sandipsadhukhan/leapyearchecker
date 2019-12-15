from tkinter import *
from tkinter import messagebox


# ********* LOGIC PART STRAT ********
# leap year or not function
def leapYearOrNot(year):
    if(year % 100 == 0):
        return (year % 400 == 0)
    else:
        return (year % 4 == 0)
# ******** LOGIC PART END **********

# *******  Linker part start *********

def check():
    inputYear = inputVar.get()
    if((not inputYear.isnumeric()) or inputYear == '' or int(inputYear)<=0 or int(inputYear)>9999):
        inputVar.set('')
        messagebox.showerror('Error', 'Please Enter a Valid Number')
    else:
        inputYearInt = int(inputYear)
        if(leapYearOrNot(inputYearInt)):
            resultVar.set(inputYear + " is a Leap Year.")
        else:
            resultVar.set(inputYear + " is not a Leap Year.")


#******** Linker end ***********

# ********* GUI PART START *********
root = Tk()
root.title("Leap Year Checker")

# default window size 
WIDTH = 500
HEIGHT = 400

# canvas frame
canvas = Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack(fill="both")
frame = Frame(canvas, bg = "#fff")
frame.place(relwidth=1, relheight=1)

# heading
heading = Label(frame, text = "Leap Year Checker", font=('verdana', 18), bg="#fff")
heading.place(relx=.2, rely=.03, relwidth=.6)

# input area
inputLabel = Label(frame, text = "Enter a Year", font=('verdana', 14), bg="#fff")
inputLabel.place(relx=.2, relwidth=.3, rely=.2)
inputVar = StringVar()
inputField = Entry(frame, textvariable=inputVar, font=('verdana', 14), bg="#fff")
inputField.place(relx=.5,relwidth=.3, rely=.2)

# check button
checkBtn = Button(frame, text="Check", font=('verdana', 13), fg="#fff", bg="tomato", command=check)
checkBtn.place(relx=.35, relwidth=.3, rely=.35)

# result
resultLabel = Label(frame, text = "Result :", font=('verdana', 14), bg="#fff", anchor="e")
resultLabel.place(relx=.1, relwidth=.2, rely=.5)
resultVar = StringVar()
resultField = Label(frame, textvariable=resultVar, font=('verdana', 14), bg="#fff", anchor="w")
resultField.place(relx=.31, relwidth=.6, rely=.5)

# copyright area
copyText = Label(frame, text = "Made with Python by Sandip sadhukhan.", bg="#fff")
copyText.place(relx=.2, relwidth=.6, rely=.8)

root.mainloop()
# ***** GUI END HERE ********