from tkinter import *
from cryptography.fernet import Fernet

# initializing root
root = Tk()

# root geometry
root.geometry("750x750")

key = Fernet.generate_key()
f = Fernet(key)


# function to show message
def message():
    encryted = f.encrypt(message.encode())
    print("encrypted message", encryted)
    decrypted = f.decrypt(encryted)
    print("decrypted message", decrypted)

message()

encrypted = StringVar()
decrypted = StringVar()

# creating an entry to take encrypt message
encryptedEntry = Entry(root, textvariable=encrypted).pack(pady=10)
# entry for decrypted message
decryptedEntry = Entry(root, textvariable=decrypted).pack(pady=10)

# button for message
Button(root, text="Message :", command=message).pack(pady=10)



root.mainloop()