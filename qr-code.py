# ask user for url
# ask user for file name

import qrcode

url = input("Enter url:")
file_name = input("Enter file name:")

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save(f"qr-img/{file_name}.png")
