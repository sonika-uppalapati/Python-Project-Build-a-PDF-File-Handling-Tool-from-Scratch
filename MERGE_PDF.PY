# building a file handling tool : creating executable ( .exe) files from python code

# example code : merging multiple PDF files


import PyPDF2
import os


def merge_pdfs(input_folder, output_pdf):
# remove the existing merged.pdf file if it exists.

    if os.path.exists(output_pdf):
        os.remove(output_pdf)

# get a list of PDF files in the input folder
    pdf_files = [file for file in os.listdir(input_folder) if file.endswith('.pdf')]

# sort the list of PDF files (this is optional)
    pdf_files.sort()

# create a PDF writer object
    pdf_writer = PyPDF2.PdfWriter() # Moved the pdf_writer initialization outside the loop
    for pdf in pdf_files:
        with open(os.path.join(input_folder, pdf), 'rb') as f:
            pdf_reader = PyPDF2.PdfReader(f) # Changed 'file' to 'f' to match the file object
            for page_num in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[page_num])

# write the merged PDF to the output file.
    with open(output_pdf, 'wb') as out:
        pdf_writer.write(out)
    print(f"Merged PDF saved as {output_pdf}")

# Let's use the above function

input_folder = 'pdf_files' # path to the folder containing PDF files to merge
output_pdf = 'pdf_files/merged.pdf' # path to the output merged PDF file

merge_pdfs(input_folder, output_pdf) # Removed extra space in 'output_pdf ' and passed the variables, not strings