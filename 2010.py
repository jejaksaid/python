import pyqrcode
url = pyqrcode.create('https://sites.google.com/view/pyqrcode/home')
print(url.terminal(quiet_zone=1))