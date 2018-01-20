import xlrd
workbook = xlrd.open_workbook('test.xls')
worksheet = workbook.sheet_by_name('Data')
print(worksheet.cell(0,0).value)
