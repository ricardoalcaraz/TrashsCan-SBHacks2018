import csv
with open('test.csv', 'r') as csvfile:
    barcodeReader = csv.reader(csvfile, delimiter='"', quotechar='|')
    for row in barcodeReader:
        print(', '.join(row))
