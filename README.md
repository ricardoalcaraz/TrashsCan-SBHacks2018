Trash sCan
==========

Inspiration
-----------

Looking around the SBHacks room for problems that needed solving, our team recognized huge amounts of trash spread throughout the room, mainly bottles and cans. We decided to make an IoT device to tackle this problem and make recycling easy, fun and efficient.

What it does and what it could do
---------------------------------

The Trash sCan scans trash barcodes to give you insight into the carbon footprint of each of your trash loads as well as the total California Refund Value accumulated in your bottles and cans separation. You can watch the money go up as you recycle!

If you are subscribed to 12-bottle boxes of Soylent from Amazon Prime, the Trash sCan will go ahead and order a new box after you've drank (and trashed) 9 or 10.

As you continue scanning items, the Trash sCan will offer tips on how to reduce your carbon footprint (e.g. "Try to use less plastic bottles"). These tips could be greatly improved if the Trash sCan was to be employed on a significant scale, collecting data, and tied to other Amazon services (e.g."There is a more environmentally friendly alternative available"). 

How we built it
---------------

A Qualcomm DragonBoard™ 410c was used for its  Wi-Fi and Bluetooth connectivity options. In our case, an Android phone is being used as the bar code reader, but an infrared barcode scanner would be built into the machine once realized. The DragonBoard runs an Apache web server to which the barcode data is sent, after which a python script fetches product details relevant to the barcode and performs all relevant operations. The user interacts with the device through an LCD screen.

Challenges we ran into
----------------------

Being a team of mostly hardware people, we had to find ways to realize our idea despite limited hardware options. Additionally, some of the manufacturer libraries for the board were outdated and so a mixture of python and C++ code had to be used to utilize all functions.

Accomplishments that we are proud of
------------------------------------

We are very proud of our idea that is both fun and could contribute to a more sustainable world. With our limited python experience and short time span we were able to create a fun demo to engage people in IoT ideas and imagine a smart future.

Rosswell is proud of his terrible trash can be smart pun.