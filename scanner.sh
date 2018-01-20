#Grab the barcode data from the web
while :
     do
wget --no-check-certificate 'https://drive.google.com/uc?export=download&id=18hGPJR1wQEjTXE18zxdnZeoWP0u99A_E' -O items.xls
#Parse the data
python main.py
#Display the data
sudo ./Display/Display
done
