from tkinter import *
from tkinter import messagebox
import pyqrcode
import os 
window = Tk()
window.title("QR Generator")

# the code

def generate():
    if len(subject.get()) != 0:
        global myQr
        myQr = pyqrcode.create(subject.get())
        qrImage = myQr.xbm(scale=6)
        global photo
        photo = BitmapImage(data=qrImage)
    else:
        message.showinfo("Error!", "Please Enter the Subject")
    try:
        showCode()
    except:
        pass

# code passing
def showCode():
    global photo
    notificationLabel.config(image=photo)
    subLabel.config(text="showing QR code for: " + subject.get())
def save():
    # folder to save all the codes
    dir = path1 = os.getcwd() + "\\QR Codes"


window.mainloop()
