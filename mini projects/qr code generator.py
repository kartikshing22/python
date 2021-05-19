import pyqrcode
from pyqrcode import QRCode

# String which represent the QR code
s = "https://github.com/kartikshing22"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the png file naming "myqr.png"
url.svg("kartikey_github.svg", scale=8)