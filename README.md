# Yaesu FT-817ND CAT Display In Python
Python implementation of CAT system for Yaesu FT-817ND.

## Overview
According to Yaesu FT-817ND's manual, the CAT System allows the transceiver to be controlled by a personal computer. The purpose of this project is to learn this system for later implementing it using an AVR microcontroller.

The program is written in Python and uses ```serial``` library to connect to the transceiver. It runs as console application in text mode.

## :warning: Important Warning!

1. This program is provided as is and I'm not responsible for any damage it may cause.
2. Before using this program make sure you completely understand what you are doing.
3. Before sending any commands to your transceiver make a backup copy of factory calibration settings in service menu. There are [sources](http://www.ka7oei.com/ft817_meow.html) which state that some commands may completely erase it. This may result in need to send the transceiver to Yaesu for realignment.

## Connecting to PC

Yaesu FT-817ND's is connected to PC through a COM port. I used one of many USB to COM boards available on eBay and AliExpress for a couple of dollars. The port is connected to ```TXD``` and ```RXD``` pins of the ```ACC``` connector located on the rear panel of the transceiver. Refer to [Yaesu FT-817ND's Operation Manual](http://www.yaesu.co.uk/files/FT-817ND_Operating%20Manual.pdf) for more details.

![ACC plug](https://raw.githubusercontent.com/4x1md/ft817_cat_python/master/images/ft817_connection.png)

Programming cable can also be used and will work fine with this program.

## Program Structure

The program is implemented as ```FT817``` class with following methods:

```__init__(self, serial_port, serial_speed, serial_stopbits)```: constructor which starts serial connection and resets transceiver state variables ```self._freq```, ```self._mode```, ```self._squelch``` and ```self._s_meter```.

```read_frequency(self)```: reads frequency and mode data and stores it in ```self._freq``` and ```self._mode``` variables.

```read_rx_status(self)```: reads receiver status (S-level, squelch state, CTCSS/DCS code match and discriminator centering) and stores S-level and squelch state in ```self._s_meter``` and ```self._squelch``` variables.

```get_s_meter_string(self, s_meter)```: generates S-meter string for second line of output.

```get_trx_state_string(self)```: generates two lines of text which include frequency, modulation, squelch level and S-meter data.

```loop(self, samples_per_sec)```: reads data from the transceiver as many times per second as defined in ```samples_per_sec``` variable.

## Program Settings And Constants

### FT817() Class

```FT817``` class contains the following settings and constants:

```SERIAL_SPEED```, ```SERIAL_STOPBITS```: COM port speed and stopbits accordingly. By default FT-817 CAT interface is set to 4800 bps with two stop bits.

```SERIAL_TIMEOUT```: sets COM port reading timeout to avoid program blocking if the transceiver is not connected to the port or is turned off.

```CMD_READ_FREQ```, ```CMD_READ_RX_STATUS```: byte sequences to send to the trasceiver to read frequency and RX status accordingly.

### trx_monitor.py

```SERIAL_PORT```: COM port name where FT-817ND transceiver is connected.

```SAMPLES_PER_SEC```: number of times per second to query the transceiver.

## Running the program

Run the ```trx_monitor.py``` file in Python interpreter.

## Program Output

The output consists of two lines which are pretty self explanatory.

```43872500Hz FM SQL: OFF```

```S3+00 |||............```

The first line shows frequency, mode (AM, FM, SSB, PKT etc.) and squelch state. The second line is S-Meter which shows S-level and dB over S9 and a simple scale where 15 dots correspond to S0 and 15 pipes correspond to S9+20dB.

Program output in console with no signal and squelch on (left) and with squelch off (right):

![Squelch on](https://raw.githubusercontent.com/4x1md/ft817_cat_python/master/images/ft817_cat_output.png)

## Questions? Suggestions?
You are more than welcome to contact me with any questions, suggestions or propositions regarding this project. You can:

1. Visit [my QRZ.COM page](https://www.qrz.com/db/4X1MD)
2. Visit [my Facebook profile](https://www.facebook.com/Dima.Meln)
3. :email: Write me an email to iosaaris =at= gmail dot com

73 de 4X1MD ex 4X5DM

![73's](https://raw.githubusercontent.com/4x1md/ft817_cat_python/master/images/73s.jpg)
