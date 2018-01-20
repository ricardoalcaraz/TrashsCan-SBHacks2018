#Grab the barcode data from the web
wget --no-check-certificate 'https://drive.google.com/uc?export=download&id=1RgsM9a7x_bQP-eHGfzWh6bvRJhEGTI1L' -O items.xls
#Parse the data
python main.py
#Display the data
sudo ./Display/Display
