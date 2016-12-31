'''
Created on Dec 31, 2016

@author: 4X5DM

@note: The program uses the FT817 class to query the transceiver and to print
       its state.
       Serial port name is defined by SERIAL_PORT constant.
       Number of queries per second is defined by SAMPLES_PER_SEC constant.
'''

from ft817 import FT817
import time

# Constants
SERIAL_PORT = "COM8"
SAMPLES_PER_SEC = 5

if __name__ == '__main__':
    print "Starting FT-817ND monitor..."
    
    try:
        ft817 = FT817(SERIAL_PORT)
        delay = 1.0 / SAMPLES_PER_SEC
        while True:
            ft817.read_frequency()
            ft817.read_rx_status()
            print
            print ft817
            time.sleep(delay)
    except KeyboardInterrupt:
        # KeyboardInterrupt exception is thrown when CTRL-C or CTRL-Break is pressed. 
        pass
    except Exception, msg:
        print "\r\nError has occured. Error message:"
        print msg
        print "\r\n"
    finally:
        print "See you later. 73!"
