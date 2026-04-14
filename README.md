# 🔲 QR Code Generator

Generate a permanent, self-hosted QR code for any URL — no third-party services, no expiry.

---

## 📋 Requirements

| Requirement | Notes |
|-------------|-------|
| [Python 3](https://www.python.org/downloads/) | Download from python.org |
| pip | Comes bundled with Python automatically |

---

## 🚀 Quick Start

### Step 1 — Install the QR library *(one time only)*

```bash
pip install qrcode[pil]
```

### Step 2 — Set your URL *(optional)*

Open `generate_qr.py` and find this line near the top:

```python
URL = "https://mamacookin.com"
```

Replace the URL with whatever website you want, then save the file.

### Step 3 — Run it

Navigate to the folder containing `generate_qr.py` and run:

```bash
python generate_qr.py
```

Your QR code will be saved in the same folder as **`my_qr_code.png`**.

### Step 4 — Change the output filename *(optional)*

In `generate_qr.py`, find:

```python
OUTPUT_FILE = "my_qr_code.png"
```

Change `"my_qr_code.png"` to any name you like, e.g. `"new_menu_qr.png"`.

---

## ❓ Does the QR code expire?

**No — it never expires.**

Because you generate it yourself (not through a third-party service), the QR code is simply a pattern that permanently encodes your URL.

It will only stop working if:

- 🔴 Your website goes offline
- 🔴 Your domain expires and isn't renewed
- 🔴 The URL changes (e.g. you move to a new site)

As long as your site is live, the QR code works **forever** — even in 10 years.

---

## 🖨️ Tips for Printing

- Print at a **minimum size of 3 × 3 cm** so phones can scan it reliably
- **Keep it square** — don't stretch or squish the image
- **Test with your phone** before printing in bulk
- Works natively with both iPhone and Android camera apps — no extra app needed

---

## ⚡ Quick Reference

```bash
# 1. Edit the URL in generate_qr.py
# 2. Save the file
# 3. Run:
python generate_qr.py
# 4. Done — my_qr_code.png is ready
```
