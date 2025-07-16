# Daily Automation Scripts

This repository contains simple Python scripts designed to automate common day-to-day tasks. Each script is standalone and comes with its own usage instructions and prerequisites.

---

## PDF Signing Script

**Description:**  
This script allows you to digitally insert an image of your signature into a PDF file at a specific placeholder (represented by a series of underscores `"______________"`). It automatically detects the placeholder and places your signature image over it.

### Prerequisites
- Python 3.7 or higher
- [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/) library  
  Install with: pip install pymupdf
- A PDF file you want to sign
- An image file of your signature (preferably PNG with transparent background)

### Usage Instructions
1. Place the following files in the **same folder**:
 - The PDF file you want to sign (e.g., `document.pdf`)
 - Your signature image file (e.g., `signature.png`)
 - The signing script file (e.g., `sign_pdf.py`)
2. Run the script using Python, specifying the input and output filenames and the signature image if necessary.
3. The script will find the first placeholder `"______________"` in the PDF and insert your signature image above it.
4. The signed PDF will be saved with the specified output filename.

### Notes
- The script searches all pages by default, but you can specify a page number to limit the search.
- Adjust the vertical offset and image size in the script if needed to better fit your signature.
- The placeholder must be text underscores, not images.

---

## General Notes

- Make sure your working directory contains all necessary files before running any script.
- All scripts are tested on Windows and Linux systems.
- Feel free to contribute by adding your own automation scripts!

---

## Contact

For questions or suggestions, please open an issue or contact me directly.


