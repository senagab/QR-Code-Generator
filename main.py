import qrcode

# url/text
qrcode_data = "Insert the website address, drive or image here"

# creates object
qr = qrcode.QRCode(
    version=1,  # qr code size (the bigger the size, the more information)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # troubleshooting
    box_size=10,
    border=4,
)

# input
qr.add_data(qrcode_data)
qr.make(fit=True)

# render
img = qr.make_image(fill_color="white", back_color="#252525")

# export
img.save("filename.png")
