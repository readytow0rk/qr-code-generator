import sys
import os

# Install required library if not present
try:
    import qrcode
except ImportError:
    os.system("pip install qrcode[pil]")
    import qrcode

# ─────────────────────────────────────────
#  EDIT THIS LINE with your URL
URL = "https://www.vistaprint.co.uk/marketing-materials/flyers/templates?attributes=size_a5%2Cproduct%20orientation_vertical%2Cfold_tri-fold&qty=5000"
#
#  EDIT THIS LINE to change output filename
OUTPUT_FILE = "my_qr_code.png"
# ─────────────────────────────────────────

qr = qrcode.QRCode(
    version=None,          # auto-pick smallest size
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # 30% damage tolerance
    box_size=10,           # pixel size of each square
    border=4,              # white quiet zone around QR
)

qr.add_data(URL)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save(OUTPUT_FILE)

print(f"Done! QR code saved as: {OUTPUT_FILE}")
print(f"URL encoded: {URL}")