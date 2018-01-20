import csv
with open('scanner.csv', 'rb') as csvfile:
    barcodeReader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in barcodeReader:
        print(', '.join(row))
