import qrcode
img = qrcode.make("https://www.instagram.com/aadesh__lokhande/")
img.save('QR.png')