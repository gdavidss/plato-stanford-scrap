import os
import pdfkit
from bs4 import BeautifulSoup
from PyPDF2 import PdfMerger
from tqdm import tqdm

def convert_html_to_pdf(source_dir, output_pdf):
    options = {
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'custom-header': [
            ('Accept-Encoding', 'gzip')
        ],
        'no-outline': None,
        'enable-local-file-access': ''
    }
    
    temp_pdfs = []  # List to keep track of individual PDF files
    merger = PdfMerger()

    for filename in tqdm(os.listdir(source_dir)):
        if filename.endswith('.html'):
            html_path = os.path.join(source_dir, filename)
            temp_pdf_path = os.path.join(source_dir, f"{filename}.pdf")
            temp_pdfs.append(temp_pdf_path)

            # Optional: Parse and clean HTML
            with open(html_path, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f, 'html.parser')

            # Here you can modify the soup object if needed

            # Convert to PDF
            pdfkit.from_string(str(soup), temp_pdf_path, options=options)

    # Merge PDFs
    for temp_pdf in temp_pdfs:
        merger.append(temp_pdf)
    
    merger.write(output_pdf)
    merger.close()

    # Optional: Cleanup temporary PDF files
    for temp_pdf in temp_pdfs:
        os.remove(temp_pdf)

# Usage
source_directory = './html'
output_pdf_filename = 'plato.pdf'
convert_html_to_pdf(source_directory, output_pdf_filename)
