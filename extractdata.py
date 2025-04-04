import pdfplumber
import pandas as pd
import os

def extract_tables_from_pdf(pdf_path, output_excel):
    with pdfplumber.open(pdf_path) as pdf:
        tables = []
        for i, page in enumerate(pdf.pages):
            extracted_tables = page.extract_tables()

            if extracted_tables and any(extracted_tables):  # If tables detected normally
                for table in extracted_tables:
                    df = pd.DataFrame(table)
                    tables.append((df, i+1))  # Store with page number
            else:  # Try extracting manually if tables aren't detected
                df = extract_borderless_table(page)
                if not df.empty:
                    tables.append((df, i+1))

    if not tables:
        print("No tables found in the PDF.")
        return
    
    save_tables_to_excel(tables, output_excel)

def extract_borderless_table(page):
    """
    Extracts tables from PDFs that do not have borders using text alignment.
    """
    words = page.extract_words()
    if not words:
        return pd.DataFrame()  # No text found

    # Sort words by vertical position (top) and then horizontal (x0)
    words.sort(key=lambda w: (w["top"], w["x0"]))
    
    rows = []
    current_row = []
    last_top = None

    for word in words:
        if last_top is None or abs(word["top"] - last_top) < 5:  # same row if close enough
            current_row.append(word["text"])
        else:
            rows.append(current_row)
            current_row = [word["text"]]
        last_top = word["top"]

    if current_row:
        rows.append(current_row)

    return pd.DataFrame(rows)

def save_tables_to_excel(tables, output_path):
    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
        for idx, (df, page) in enumerate(tables, start=1):
            df.to_excel(writer, sheet_name=f"Page_{page}_Table_{idx}", index=False, header=False)
    print(f" Tables successfully saved to: {output_path}")


pdf_file = "test1.pdf"
output_excel = "extracted_tables.xlsx"


extract_tables_from_pdf(pdf_file, output_excel)
