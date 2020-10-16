import PyPDF2
import sys

# Get the target file and the desired name of the output file
target_file = input('What file would you like to add a watermark to? :')
dest_file = input('Name the new file. The .pdf is not needed:')

# Open the target file
template = PyPDF2.PdfFileReader(open(target_file, 'rb'))

# Load the desired watermark file. Make sure
# to add the path and filename
watermark = PyPDF2.PdfFileReader(open('PATH/TO/WATERMARK/FILE.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

# Add the watermark and output to the input name
for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open(f'{dest_file}.pdf', 'wb') as file:
        output.write(file)
