/*
 * Authors: Ricardo Alcaraz, Jaap De Dood, Rosswell Tiangco
 */

#include <string>
#include "upm/jhd1313m1.hpp"
#include <iostream>
#include <iomanip>
#include <fstream>
#include <boost/lexical_cast.hpp>

#define I2C_BUS 0
#define RGB_WHT 0xff,0xff,0xff
#define RGB_RED 0xff,0x00,0x00
#define RGB_GRN 0x00,0xff,0x00
#define RGB_BLU 0x00,0x00,0xff
#define SLEEP_TIME 1

using namespace std;
upm::Jhd1313m1* lcd;

/**Function to display text on I2C LCD Screen*/
void display(string str1, string str2, int red, int green, int blue) {
	lcd->clear();
	lcd->setColor(red, green, blue);
	lcd->setCursor(0,0); /* first row */
	lcd->write(str1);
	lcd->setCursor(1,2); /* second row */
	lcd->write(str2);
	sleep(SLEEP_TIME);
}

void printToScreen() {
	/*Initialize variable names*/
 	string line1;
	string line2;
	/*File to read from*/
	ifstream myfile("toLCD.txt");
	if(myfile.is_open()) {
		getline(myfile,line1);
		getline(myfile,line2);
		double co2 = boost::lexical_cast<double>(line1);
		//Will display slightly redder as the carbon footprint goes up
		if(co2 > 0.0) {
			int blue = 255 - (int) co2;
			int green = 255 - (int) co2;
		}else {
			int blue = 0;
			int green = 0;
		}
		display("CO2: "+ line1+"kg", "CRV: $" + line2, RGB_WHT);
		co2 = boost::lexical_cast<double>(line1);
		display("CO2: "+ line1, "CRV: " + line2, RGB_WHT);
	} else {
		display("Unable to open file", "", RGB_RED);
	}
}

/**Will read the first two lines of a text file and output it onto the LCD screen*/
int main(int argc, char* argv[]) {
	/*Initialize LCD screen address*/
	lcd = new upm::Jhd1313m1(I2C_BUS, 0x3e, 0x62);
	printToScreen();
	/*Clear memory and empty out LCD screen*/
        /* Commented out to keep screen on while fetching new data */
	/* delete lcd; */ 

	return 0;
}


