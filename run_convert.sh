#!/bin/bash
PROJ_DIR="/home/hfaria/Projeto/BigPDF2MD"
VENV_PYTHON="$PROJ_DIR/venv/bin/python"
CONVERT_SCRIPT="$PROJ_DIR/convert.py"

"$VENV_PYTHON" "$CONVERT_SCRIPT" "$1"
