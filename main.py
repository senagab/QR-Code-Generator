import qrcode

# url/texto
dados_para_qrcode = "insira aqui o endereço do site, drive, imagem"

# cria objeto
qr = qrcode.QRCode(
    version=1,  # tamanho do qr code (quanto maior, mais informação)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # troubleshooting
    box_size=10,
    border=4,
)

# input
qr.add_data(dados_para_qrcode)
qr.make(fit=True)

# render
img = qr.make_image(fill_color="white", back_color="#252525")

# export
img.save("bascuare-invert.png")
