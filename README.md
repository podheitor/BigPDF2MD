<div align="center">
  <h1>🚀 BigPDF2MD & MD2PDF Integration</h1>
  <p><b>The ultimate two-way document converter for KDE Plasma (Dolphin)</b></p>
  <img src="https://img.shields.io/badge/OS-BigLinux-blue?style=for-the-badge&logo=linux" alt="BigLinux">
  <img src="https://img.shields.io/badge/Desktop-KDE%20Plasma-blue?style=for-the-badge&logo=kde" alt="KDE">
  <img src="https://img.shields.io/badge/Python-3.x-yellow?style=for-the-badge&logo=python" alt="Python">
</div>

---

## ✨ Features

- 📄 **PDF ➡️ Markdown (MD):** Convert heavy PDF documents into clean, readable, and structured Markdown files. Powered by `pymupdf4llm` for the highest quality text extraction.
- 📝 **Markdown (MD) ➡️ PDF:** Convert your `.md` documentation directly into beautiful `.pdf` files.
- 🖱️ **One-Click Integration:** Native integration with Dolphin via KDE Service Menus. Just right-click!
- 🔔 **System Notifications:** Seamlessly integrated with KDE notifications to let you know when conversions start and finish.
- 📦 **Sandboxed Environment:** Safely installs dependencies in a Python Virtual Environment (`/opt/BigPDF2MD/venv`) without polluting your system.

## 📥 Installation

### 🏆 Recommended: Pre-Built Arch Package (BigLinux)

1. Download the latest `bigpdf2md-1.1-1-any.pkg.tar` from the [Releases](#).
2. Install it using `pacman` or just double click it in Dolphin:
```bash
sudo pacman -U bigpdf2md-1.1-1-any.pkg.tar
```

### 🔧 Manual Build from Source

You can build the Arch package yourself using `makepkg`:
```bash
git clone https://github.com/podheitor/BigPDF2MD.git
cd BigPDF2MD
makepkg -si
```

## 🛠️ Usage Guide

1. Open your **Dolphin File Manager**.
2. Find any `.pdf` or `.md` file.
3. **Right-click** on the file:
   - For PDFs: Select **Convert PDF to Markdown (MD)**
   - For MDs: Select **Convert Markdown (MD) to PDF**
4. Wait a few moments. A system notification will pop up when it's done!

---
*Developed with ❤️ for the BigLinux & KDE Community.*
