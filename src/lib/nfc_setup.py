import sys

import board
import busio
from adafruit_pn532.i2c import PN532_I2C
from digitalio import DigitalInOut


class NFCUtils:

    def start_i2c(self):
        # I2C connection:
        i2c = busio.I2C(board.SCL, board.SDA)

        reset_pin = DigitalInOut(board.D6)
        req_pin = DigitalInOut(board.D12)
        pn532 = PN532_I2C(i2c, debug=False, reset=reset_pin, req=req_pin)

        ic, ver, rev, support = pn532.firmware_version
        print("[i] Found PN532 with firmware version: {0}.{1}".format(ver, rev))
        sys.stdout.flush()

        # Configure PN532 to communicate with MiFare cards
        pn532.SAM_configuration()

        return pn532
