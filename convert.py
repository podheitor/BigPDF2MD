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
        print("Usage: python convert.py <file.pdf>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    if not os.path.exists(pdf_path):
        send_notification("PDF to MD Error", f"File not found: {pdf_path}", "dialog-error")
        sys.exit(1)

    if not pdf_path.lower().endswith(".pdf"):
        send_notification("PDF to MD Error", f"Not a PDF file: {pdf_path}", "dialog-error")
        sys.exit(1)

    base_name = os.path.splitext(pdf_path)[0]
    md_path = f"{base_name}.md"

    send_notification("PDF to MD Conversion", f"Starting conversion for {os.path.basename(pdf_path)}...")

    try:
        import pymupdf4llm
        # Perform conversion
        md_text = pymupdf4llm.to_markdown(pdf_path)
        
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(md_text)
            
        send_notification("PDF to MD Conversion", f"Successfully converted to {os.path.basename(md_path)}", "dialog-success")
    except Exception as e:
        send_notification("PDF to MD Error", f"Failed to convert: {str(e)}", "dialog-error")
        sys.exit(1)

if __name__ == "__main__":
    main()
