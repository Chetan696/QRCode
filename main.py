import qrcode
import qrcode as qr
from PIL import Image
qr=qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data("https://www.linkedin.com/in/chetan-gudditi-922b38272/")
qr.make(fit=True)
img=qr.make_image(fill_color="Red",back_color="white")
img.save("LinkedinQR-Color.png")