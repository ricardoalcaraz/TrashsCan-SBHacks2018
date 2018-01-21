import xlrd
#Reads the xls files and returns it as an object
def parseItems(fileName):
    book = xlrd.open_workbook(fileName)
    sheet = book.sheet_by_index(0)
    return sheet


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

def getCarbon(total):
  totalCarbon = 0
  for item in total:
    totalCarbon += (float(item.getCount()) * float(item.getCarbon()))
  return totalCarbon

def getCRV(total):
  totalCRV = 0
  for item in total:
    totalCRV += (float(item.getCount()) * float(item.getCRV()))
  return totalCRV

#Download item from web
#url = 'http://drive.google.com/uc?export=download&id=18hGPJR1wQ    EjTXE18zxdnZeoWP0u99A_E'

#urllib.request.urlretrieve(url, 'items.xls')
#Reads data from barcode
sheet = parseItems("items.xls") 


itemList = []
#Iterate through all the items and do something with it
for rows in range(sheet.nrows):
    rowList = []
    cells = sheet.row_slice(rows, 0, 6)
    for cell in cells:
        #print(cell.value)
        rowList.append(cell.value)
    itemList.append(rowList)


total = []
display = open('toLCD.txt','w')
del itemList[0]
for line in itemList:
    total.append( Item(line[0],line[1],line[2],line[3],line[4],line[5]) )
    display.write('CO2: ' + str(round(getCarbon(total),2))+'\n')
    display.write('CRV: ' + str(round(getCRV(total),2))+'\n')

