'''import xlrd
#Reads the xls files and returns it as an object

clearTotalFlag = False
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
  if total == 0:
    return 0
  totalCarbon = 0
  for item in total:
    totalCarbon += (float(item.getCount()) * float(item.getCarbon()))
  return totalCarbon

def getCRV(total):
  if total == 0:
    return 0
  totalCRV = 0
  for item in total:
    totalCRV += (float(item.getCount()) * float(item.getCRV()))
  return totalCRV

#Download item from web
#url = 'http://drive.google.com/uc?export=download&id=18hGPJR1wQ    EjTXE18zxdnZeoWP0u99A_E'

#urllib.request.urlretrieve(url, 'items.xls')
#Reads data from barcode
#sheet = parseItems("items.xls")


itemList = []
#Iterate through all the items and do something with it
def addToSheet():
    sheet = parseItems("items.xls")
    for rows in range(sheet.nrows):
        rowList = []
        cells = sheet.row_slice(rows, 0, 6)
        for cell in cells:
            #print(cell.value)
            rowList.append(cell.value)
        itemList.append(rowList)

def clearSheet():
  if (True): #If button high
     sheet = parseItems("items.xls")
     for rows in range(sheet.nrows):
        rowList = []
        cells = sheet.row_slice(rows, 0, 6)
        for cell in cells:

            cell.value = None
     return True
  else:
     return False


addToSheet()


clearTotalFlag = clearSheet()
if (clearTotalFlag):
    total = 0
else:
    total = []
    del itemList[0]
    for line in itemList:
        total.append( Item(line[0],line[1],line[2],line[3],line[4],line[5]) )

display = open('toLCD.txt','w')
if (getCarbon(total) == 0):
    display.write(str(0))
else:
    display.write(str(format(getCarbon(total),'.2f'))+'\n')
if (getCRV(total) == 0):
    display.write(str(0))
else:
    display.write(str(format(getCRV(total),'.2f'))+'\n')

print(getCarbon(total))
clearSheet();
print(getCarbon(total))
print(getCarbon(total))
'''


import csv
import datakick

itemList = []


with open('barcodes.csv', 'r') as f:
    reader = csv.reader(f)
    barcodeList = list(reader) #contains every barcode in .csv

    for row in barcodeList:
        for col in row:
            if col == '':
                break
            barcode = col
            product = datakick.find_product(barcode)
            itemList.append(product)
    print(barcodeList)


def getCRV(item):
  if "oz" in item.size:
    if int(item.size[0:2]) < 24:
      return 0.05
    else:
      return 0.1
  else:
    return 0

def getCarbonFootprint(item):
  return 82.8

def getTotalCRV(itemList):
 totalCRV = 0
 for item in itemList:
   totalCRV += getCRV(item)
 return totalCRV


def getTotalCarbonFootprint(itemList):
  carbonFootprint = 0
  for item in itemList:
    carbonFootprint += getCarbonFootprint(item)
  return carbonFootprint


print(getTotalCRV(itemList))
print(getTotalCarbonFootprint(itemList))


display = open('toLCD.txt','w')
'''
if (getCarbonFootprint(itemList) == 0):
    display.write(str(0))
else:
    display.write(str(format(getCarbon(total),'.2f'))+'\n')
if (getCRV(total) == 0):
    display.write(str(0))
else:
    display.write(str(format(getCRV(total),'.2f'))+'\n')
'''

display.write(str(format(getCarbonFootprint(itemList),'.2f'))+'\n')
display.write(str(format(getTotalCRV(itemList)),'.2f'))+'\n')