# importing tkinter
from tkinter import *

# importing pyshorteners
import pyshorteners

# initializing root
root = Tk()

# setting geometry
root.geometry("400x300")


url = input("Enter your URL")
s = pyshorteners.Shortener().tinyurl.short(url)
print("Your URL is ready: ", s)

root.mainloop()
