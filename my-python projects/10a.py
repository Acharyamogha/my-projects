import PyPDF2

# List of PDF files and page ranges to include
pdfs = [
    
    {"file": "file1.pdf", "pages": (1, 3)},
    {"file": "file2.pdf", "pages": (2, 4)},
    # Add more PDFs and page ranges as needed
]

# Create a PDF writer object
output_pdf = PyPDF2.PdfWriter()

# Loop through each PDF and extract specified pages
for pdf_info in pdfs:
    pdf_file = pdf_info["file"]
    start_page, end_page = pdf_info["pages"]

    # Open the source PDF
    with open(pdf_file, "rb") as pdf:
        pdf_reader = PyPDF2.PdfReader(pdf)

        # Loop through the specified pages and add them to the output PDF
        for page_num in range(start_page - 1, end_page):  # Page numbers are 0-based
            output_pdf.add_page(pdf_reader.pages[page_num])

# Save the combined PDF
output_filename = "combined_pages.pdf"
with open(output_filename, "wb") as output:
    output_pdf.write(output)

print("Combined PDF saved as:", output_filename)