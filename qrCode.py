import qrcode

input = input("Enter text for QR Code Generation: ")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
print(input)
text2 = "upi://pay?pa={upiId}&amp;pn=WSFX GLOBAL PAY&am=0&amp;cu=INR".format(upiId =input)
qr.add_data(text2)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
fileName =input+".png"
img.save(fileName)