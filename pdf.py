import PyPDF2

with open('./pdf/dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    # print(reader.numPages)
    # print(reader.getPage(0))
    page = reader.getPage(0)
    page.rotateCounterClockwise(180)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('./pdf/tilt.pdf', 'wb') as new_file:
        writer.write(new_file)
