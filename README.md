# MSCS633 Hands-On Assignment2: Construct AI QR Code Generator with Python

This project constructs a Python application that generates a QR code when given a URL. For demonstration, the application encodes the Biox Systems website address into a machine-readable QR image.

## Files

- qr_generator.py: Python source code implementing the QR code generator
- requirements.txt: Manifest file listing required Python libraries
- report.docx: Final written report with environment setup, instructions, screenshot, and GitHub URL
- output/biox_qr.png: Sample QR code image generated from https://www.bioxsystems.com/

## How to Run

### activate your virtual environment
`source .venv/bin/activate`

### install dependencies
`pip install -r requirements.txt`

### generate a QR code (will save to output/biox_qr.png and open in Preview)
`python qr_generator.py --data "https://www.bioxsystems.com/" --out output/biox_qr.png --show`

## Summary
- The application uses the qrcode and Pillow libraries to encode a given URL into a PNG QR code image.
- Command line arguments allow customizing error correction, box size, and border size.
- The generated PNG can be scanned by any QR-capable device to open the target URL.
- The included sample demonstrates encoding the Biox Systems homepage.
