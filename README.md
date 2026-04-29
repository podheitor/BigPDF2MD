# BigPDF2MD

BigPDF2MD is a simple integration tool for KDE Plasma (Dolphin) specifically designed for BigLinux (and other Arch-based distros) to convert PDF files into Markdown (.md) with a single right-click.

It leverages the powerful `pymupdf4llm` library to extract high-quality markdown, making it ideal for LLMs and documentation purposes.

## Features
- **One-Click Conversion:** Right-click any PDF in Dolphin and select "Convert PDF to Markdown (MD)".
- **High Quality:** Uses `pymupdf4llm` for superior markdown formatting.
- **System Notifications:** Integrates with KDE notifications to let you know when the conversion starts and finishes.
- **Isolated Environment:** Installs dependencies in a Python Virtual Environment to keep your system clean.

## Installation

### Manual Installation
Clone this repository and run the install script:
```bash
git clone https://github.com/podheitor/BigPDF2MD.git
cd BigPDF2MD
chmod +x install.sh
./install.sh
```

### BigLinux / Arch Linux Package (pacman)
You can build the Arch package using `makepkg`:
```bash
git clone https://github.com/podheitor/BigPDF2MD.git
cd BigPDF2MD
makepkg -si
```

## Usage
1. Open the Dolphin File Manager.
2. Find a `.pdf` file.
3. Right-click the file and select **Convert PDF to Markdown (MD)**.
4. Wait for the success notification. The `.md` file will be created in the same folder.
