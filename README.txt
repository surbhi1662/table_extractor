PROJECT README

Title: PDF Table Extractor  
Developer: Surbhi  
Program: Master of Computer Applications (MCA) – Final Year  
Institute: National Institute of Technology, Allahabad

---

 Project Overview

This is a Python-based tool designed to detect and extract tables from system-generated PDF documents without using Tabula or Camelot. The tool supports extraction of tables with borders, without borders, and with irregular structures, and saves them in Excel format.

---

 Features

- Detects and extracts tables from system-generated PDF files.
- Handles tables with borders, no borders, and irregular shapes.
- Maintains row-column structure including merged and multiline cells.
- Exports each extracted table into a neatly formatted Excel sheet.
- Includes robust error handling for invalid and unsupported files.

---

 Technologies Used

- Python 3.x  
- pdfplumber – For reading and parsing PDF content  
- pandas – For manipulating extracted table data  
- openpyxl – For writing to Excel files  
- numpy – For numerical operations (if used)

---

Setup Instructions

1. Install Python (version 3.x recommended).
2. (Optional) Create and activate a virtual environment:
   - Windows:
     ```
     python -m venv venv
     venv\Scripts\activate
     ```
   - Linux/Mac:
     ```
     python3 -m venv venv
     source venv/bin/activate
     ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

---
 How to Use

1. Place your input PDF files inside the `assets/` folder.
2. Run the main script:
   ```
   python table_extractor.py
   ```
3. Extracted Excel files will be saved in the `output/` folder.

---

Project Folder Structure

```
table_extractor/
│
├── assets/              --> Input PDF files
├── output/              --> Output Excel files
├── table_extractor.py   --> Main Python script
├── requirements.txt     --> List of dependencies
└── README.txt           --> Project documentation (this file)
```

---

Error Handling

This tool gracefully handles:
- Invalid or corrupted PDF files
- PDFs without any tables
- Files with unsupported formats or missing permissions

---

 Limitations

- Designed specifically for system-generated (non-scanned) PDFs.
- May need manual verification for very complex or nested table structures.
- Performance may vary depending on the size and layout complexity of the PDF.

---

 Acknowledgment

This project was created as part of an academic assignment on document data extraction using Python.

---


