━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  QR CODE GENERATOR — INSTRUCTIONS
  File: generate_qr.py
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT YOU NEED INSTALLED
───────────────────────
• Python 3  →  https://www.python.org/downloads/
• pip       →  comes with Python automatically


STEP 1 — INSTALL THE QR LIBRARY (one time only)
────────────────────────────────────────────────
Open your terminal and run:

    pip install qrcode[pil]

You only ever need to do this once.


STEP 2 — CHANGE THE URL (optional)
────────────────────────────────────
Open generate_qr.py in Sublime Text.
Find this line near the top:

    URL = "https://mamacookin.com"

Replace the URL with whatever website you want.
Save the file (Ctrl+S or Cmd+S).


STEP 3 — RUN IT
───────────────
In your terminal, navigate to the folder where
generate_qr.py is saved, then run:

    python generate_qr.py

The QR code image will appear in the same folder
as a file called:  my_qr_code.png


STEP 4 — CHANGE OUTPUT FILENAME (optional)
───────────────────────────────────────────
In generate_qr.py, find this line:

    OUTPUT_FILE = "my_qr_code.png"

Change "my_qr_code.png" to whatever name you like.
Example:  "new_menu_qr.png"


DOES THE QR CODE EXPIRE?
─────────────────────────
NO. Your QR code never expires.

Because you're generating it yourself (not using
a third-party service), the QR code is just a
pattern that permanently encodes your URL.

It will stop working ONLY if:
  • Your website (mamacookin.com) goes offline
  • Your domain expires and you don't renew it
  • The URL changes (e.g. you move to a new site)

As long as mamacookin.com is live, the QR works
forever — even in 10 years.


TIPS FOR PRINTING
─────────────────
• Print at minimum 3x3 cm so phones can scan it
• Don't stretch or squish the image — keep it square
• Test it with your phone before printing in bulk
• Both iPhone and Android camera apps scan it natively
  (no extra app needed)


QUICK REFERENCE
───────────────
To generate a new QR:
  1. Edit URL = "..." in generate_qr.py
  2. Save the file
  3. Run:  python generate_qr.py
  4. Done — my_qr_code.png is ready

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
