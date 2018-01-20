import xlrd

#Reads the xls files and returns it as an object
def parseItems(fileName):
    book = xlrd.open_workbook(fileName)
    sheet = book.sheet_by_index(0)
    return sheet

#Reads data from barcode
sheet = parseItems("items.xls") 

#Iterate through all the items and do something with it
for rows in range(sheet.nrows):
    cells = sheet.row_slice(rows, 0, 5)
    for cell in cells:
        print(cell.value)
