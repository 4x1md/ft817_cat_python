'''
Created on 06 May 2016

@author: Dmitry Melnichansky 4Z7DTF
'''

#from serial import *
import serial
import time

# Constants
CONN_PORT = "COM11"
CONN_SPEED = 4800
CONN_STOPBITS = serial.STOPBITS_TWO
MODES = ["LSB", "USB", "CW", "CWR", "AM", None, "WFM", None, "FM", None, "DIG", None, "PKT"]
CMD_GET_FREQ = [0x00, 0x00, 0x00, 0x00, 0x03]

SAMPLES_PER_SEC = 1

class FT817:
    def __init__(self):
        print "Starting Yaesu FT-817ND..."
        self._ser = serial.Serial(CONN_PORT, CONN_SPEED, stopbits=CONN_STOPBITS)
        self._freq = ""
        self._mode = ""
        
    def get_rx_freq(self):
        '''Sends the command to query the RX frequency and mode.
        The response is 5 bytes: first four store frequency and
        the fifth stores mode (AM, FM, SSB etc.)
        '''
        cmd = CMD_GET_FREQ
        self._ser.write(cmd)
        resp = self._ser.read(5)
        resp_bytes = (ord(resp[0]), ord(resp[1]), ord(resp[2]), ord(resp[3]))
        self._freq = "%02x%02x%02x%02x" % resp_bytes
        self._mode = MODES[ord(resp[4])]
    
    def print_data(self):
        '''Prints data.
        '''
        print "%sHz %s" % (self._freq, self._mode)
    
    def loop(self, samples_per_sec):
        '''Infinite loop which queries the transceiver and prints the data.
        Number of queries per second is passed in samples_per_sec variable.
        '''
        delay = 1.0 / samples_per_sec
        while True:
            self.get_rx_freq()
            self.print_data()
            time.sleep(delay)

if __name__ == '__main__':
    ft817 = FT817()
    ft817.loop(SAMPLES_PER_SEC)
