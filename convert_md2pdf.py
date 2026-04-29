import sys
import os
import subprocess

def send_notification(title, message, icon="dialog-information"):
    try:
        subprocess.run(["notify-send", "-i", icon, title, message])
    except Exception:
        pass

def main():
    if len(sys.argv) < 2:
        print("Usage: python convert_md2pdf.py <file.md>")
        sys.exit(1)

    md_path = sys.argv[1]
    if not os.path.exists(md_path):
        send_notification("MD to PDF Error", f"File not found: {md_path}", "dialog-error")
        sys.exit(1)

    if not md_path.lower().endswith(".md"):
        send_notification("MD to PDF Error", f"Not an MD file: {md_path}", "dialog-error")
        sys.exit(1)

    base_name = os.path.splitext(md_path)[0]
    pdf_path = f"{base_name}.pdf"

    send_notification("MD to PDF Conversion", f"Starting conversion for {os.path.basename(md_path)}...")

    try:
        from md2pdf.core import md2pdf
        md2pdf(pdf_path, md_content=None, md_file_path=md_path, css_file_path=None, base_url=None)
        
        send_notification("MD to PDF Conversion", f"Successfully converted to {os.path.basename(pdf_path)}", "dialog-success")
    except Exception as e:
        send_notification("MD to PDF Error", f"Failed to convert: {str(e)}", "dialog-error")
        sys.exit(1)

if __name__ == "__main__":
    main()
