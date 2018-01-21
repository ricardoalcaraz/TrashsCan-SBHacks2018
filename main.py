import xlrd
import mraa
import csv
import datakick 
import re
#Reads the xls files and returns it as an object

#Setting up the touch button
touch = mraa.Gpio(29)
touch.dir(mraa.DIR_IN)

isTouched = int(touch.read())
#if(isTouched):

itemList = []


with open('/var/www/html/barcodes.csv', 'r') as f:
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
    if int(re.sub("[^0-9]", "", item.size[0:2])) < 24:
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
display.write(str(format(getTotalCRV(itemList),'.2f'))+'\n')
