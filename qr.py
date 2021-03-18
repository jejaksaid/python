import pyqrcode
from PIL import Image

# insert logo or pict
logo = Image.open('syekhalijaber.png')

# size
basewidth = 75
wpercent = (basewidth/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)

# qr code
qr_big = pyqrcode.QRCode(error_correction=pyqrcode.constants.ERROR_CORRECT_H)
qr_big.add_data('https://google.com')
qr_big.make()
img_qr_big = qr_big.make_image(fill_color='#0B4E39', back_color="white").convert('RGB')
pos = ((img_qr_big.size[0] - logo.size[0]) // 2, (img_qr_big.size[1] - logo.size[1]) // 2)
img_qr_big.paste(logo, pos)
img_qr_big.save('syekhalijaber_qr.jpg')
