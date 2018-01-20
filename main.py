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
 
print(itemList[1])


#TODO Data to go to LCD should be written to a file in pairs. The file should be called "toLCD.txt"


class Item():
  def __init__(self,barcode,itemName,dateScanned,crv,carbon):
    self.__barcode = barcode
    self.__itemName = itemName
    self.__dateScanned = dateScanned
    self.__crv = crv
    self.__carbon = carbon
  def getCRV(self):
    return self.__crv
  def getCarbon(self):
    return self.__carbon    


yerba = Item(1110,"mate","01/11/10",15,4.5)

jaap = [yerba,yerba,yerba]



def getCRV(person):
  totalCRV = 0
  for item in person:
    totalCRV+=item.getCRV()
  return totalCRV
  
def getCarbon(person):
  totalCarbon = 0
  for item in person:
    totalCarbon+=item.getCarbon()
  return totalCarbon    
    
print(getCarbon(jaap))
print(getCRV(jaap))
