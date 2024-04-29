import os
from PyPDF2 import PdfReader, PdfWriter

path = "C:/Users/User/Documents/New folder/SKC/"
pdf_file_path = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and f.lower().endswith('.pdf')]
output_folder_path = "C:/Users/User/Documents/New folder/SKC/"


for file in pdf_file_path:
    file_base_name = file.replace('.pdf', '')

    pdf = PdfReader(path + file)

    no = 1
    for page_num in range(0, len(pdf.pages)):
        pdfWriter = PdfWriter()

        pdfWriter.add_page(pdf.pages[page_num])

        with open(os.path.join(output_folder_path, '{0}_{1}.pdf'.format(file_base_name, no)), 'wb') as f:
            pdfWriter.write(f)

        no = no + 1

f.close()

