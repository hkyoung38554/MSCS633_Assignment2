#!/usr/bin/env python3
import argparse
from pathlib import Path

try:
    import qrcode
    from PIL import Image
except Exception:
    print("[!] Missing dependencies. Run: pip install qrcode[pil] pillow")
    raise

def build_qr(data: str, box_size: int = 10, border: int = 4, error_correction: str = "M") -> Image.Image:
    ec_map = {
        "L": qrcode.constants.ERROR_CORRECT_L,
        "M": qrcode.constants.ERROR_CORRECT_M,
        "Q": qrcode.constants.ERROR_CORRECT_Q,
        "H": qrcode.constants.ERROR_CORRECT_H,
    }
    if error_correction not in ec_map:
        raise ValueError("error_correction must be one of L/M/Q/H")

    qr = qrcode.QRCode(
        version=None,
        error_correction=ec_map[error_correction],
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    return img

def save_qr(img: Image.Image, out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(out_path, format="PNG")

def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="AI QR Code Generator (Biox Systems)")
    p.add_argument("--data","-d", help="URL or text to encode. If omitted, will prompt.")
    p.add_argument("--out","-o", default="qr_code.png", help="Output PNG path")
    p.add_argument("--box-size", type=int, default=10, help="Pixel size of each QR box")
    p.add_argument("--border", type=int, default=4, help="Border width in boxes")
    p.add_argument("--ec", choices=["L","M","Q","H"], default="M", help="Error correction level")
    p.add_argument("--show", action="store_true", help="Open the image after saving.")
    args = p.parse_args(argv)

    data = args.data or input("Enter the URL or text to encode: ").strip()
    if not data:
        print("[!] No data provided; exiting.")
        return 2

    img = build_qr(data=data, box_size=args.box_size, border=args.border, error_correction=args.ec)
    out_path = Path(args.out)
    save_qr(img, out_path)
    print(f"[+] QR code saved to: {out_path.resolve()}")
    if args.show:
        img.show()
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
