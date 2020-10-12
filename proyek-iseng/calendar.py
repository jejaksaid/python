import tkinter # note that module name has changed from Tkinter in Python 2 to tkinter in Python 3
import calendar

top = tkinter.Tk()
# Code to add widgets will go here...
top.tittle("Calendar")
#year
year = 2020
#storing at new variable
myCal = calendar.calendar(year)
# showing data using label widget
cal_year = Label(top, text=myCal, font="Consolas 10 bold")
#packing the label widget
cal_year.pack()

top.mainloop()
