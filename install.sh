#!/bin/bash

# Define paths
PROJ_DIR="/home/hfaria/Projeto/BigPDF2MD"
VENV_DIR="$PROJ_DIR/venv"
CONVERT_SCRIPT="$PROJ_DIR/convert.py"

# Desktop file content
DESKTOP_FILE_NAME="pdf2md.desktop"

# Determine KDE ServiceMenu locations
KDE5_DIR="$HOME/.local/share/kservices5/ServiceMenus"
KDE6_DIR="$HOME/.local/share/kio/servicemenus"

echo "Creating python virtual environment..."
python3 -m venv "$VENV_DIR"

echo "Installing pymupdf4llm..."
"$VENV_DIR/bin/pip" install pymupdf4llm

echo "Generating KDE Service Menu configuration..."

# Create a shell wrapper for the desktop file to ensure it runs inside the venv
WRAPPER_SCRIPT="$PROJ_DIR/run_convert.sh"
cat << 'EOF' > "$WRAPPER_SCRIPT"
#!/bin/bash
PROJ_DIR="/home/hfaria/Projeto/BigPDF2MD"
VENV_PYTHON="$PROJ_DIR/venv/bin/python"
CONVERT_SCRIPT="$PROJ_DIR/convert.py"

"$VENV_PYTHON" "$CONVERT_SCRIPT" "$1"
EOF

chmod +x "$WRAPPER_SCRIPT"

# Generate the .desktop file content
cat << EOF > "$DESKTOP_FILE_NAME"
[Desktop Entry]
Type=Service
ServiceTypes=KonqPopupMenu/Plugin
MimeType=application/pdf;
Actions=convertToMd;
X-KDE-Priority=TopLevel

[Desktop Action convertToMd]
Name=Convert PDF to Markdown (MD)
Icon=text-markdown
Exec=$WRAPPER_SCRIPT "%f"
EOF

# Install for KDE Plasma 5
mkdir -p "$KDE5_DIR"
cp "$DESKTOP_FILE_NAME" "$KDE5_DIR/"
echo "Installed ServiceMenu to $KDE5_DIR"

# Install for KDE Plasma 6
mkdir -p "$KDE6_DIR"
cp "$DESKTOP_FILE_NAME" "$KDE6_DIR/"
echo "Installed ServiceMenu to $KDE6_DIR"

echo "Setup complete! You should now be able to right-click a PDF file in Dolphin and select 'Convert PDF to Markdown (MD)'."
