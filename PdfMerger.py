import PyPDF2
import sys

# Take in the target pdf file at the command line
inputs = sys.argv[1:]

# Ask for the name of the output file
name = input('What would you like to call your merged file? : ')


# Merge all files into one
def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write(f'{name}.pdf')


pdf_combiner(inputs)
