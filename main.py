import xlrd

#Reads the xls files and returns it as an object
def parseItems(fileName):
    book = xlrd.open_workbook(fileName)
    sheet = book.sheet_by_index(0)
    return sheet

#Reads data from barcode
sheet = parseItems("items.xls") 


itemList = []
#Iterate through all the items and do something with it
for rows in range(sheet.nrows):
    rowList = []
    cells = sheet.row_slice(rows, 0, 5)
    for cell in cells:
        #print(cell.value)
        rowList.append(cell.value)
    itemList.append(rowList)


#TODO Data to go to LCD should be written to a file in pairs. The file should be called "toLCD.txt"


class Item():
  def __init__(self,barcode,itemName,count,dateScanned,crv,carbon):
    self.__barcode = barcode
    self.__itemName = itemName
    self.__count = count
    self.__dateScanned = dateScanned
    self.__crv = crv
    self.__carbon = carbon
  def getCount(self):
    return self.__count
  def getCRV(self):
    return self.__crv
  def getCarbon(self):
    return self.__carbon    


total = []
for line in itemList:
    total.append( Item(line[0],line[1],line[2],line[3],line[4],line[5]) )


def getCRV(total):
  totalCRV = 0
  for item in total:
    totalCRV += (item.getCount() * item.getCRV())
  return totalCRV

print(getCRV(total))

def getCarbon(total):
  totalCarbon = 0
  for item in total:
    totalCarbon += (item.getCount() * item.getCarbon())
  return totalCarbon

print(getCarbon(total))
