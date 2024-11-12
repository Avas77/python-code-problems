# ask user for url
# ask user for file name

import qrcode

number = input("How many qr codes do you want?")
files = {}

for i in range(int(number)):
    print(f"Enter details for Qr code no. {i + 1}")
    url = input("Enter url:")
    file_name = input("Enter file name:")
    color = input("Enter the QR code color:")
    if file_name in files.keys():
        print("Filename already exists")
    else:
        files[file_name] = url

for file_name, url in files.items():
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"qr-img/{file_name}.png")
    print(f"{file_name} image is saved.")
