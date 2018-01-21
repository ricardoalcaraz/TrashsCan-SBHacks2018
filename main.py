import xlrd
import mraa
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

#Setting up the touch button
touch = mraa.Gpio(29)
touch.dir(mraa.DIR_IN)

isTouched = int(touch.read())
#if(isTouched):
