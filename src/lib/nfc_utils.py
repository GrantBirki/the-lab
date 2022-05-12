import board
import busio
from adafruit_pn532.i2c import PN532_I2C
from digitalio import DigitalInOut


class NFCUtils:

    def __init__(self, log):
        self.pn532 = self.start_i2c()
        self.log = log

    def scan(self):
        uid = self.pn532.read_passive_target(timeout=0.5)

        if uid is None:
            return None

        card_id = ""
        for id in uid:
            card_id += str(id)
        card_id = int(card_id)

        self.log.info(f"Found card with UID: {card_id}")

        return card_id

    def start_i2c(self):
        # I2C connection:
        i2c = busio.I2C(board.SCL, board.SDA)

        reset_pin = DigitalInOut(board.D6)
        req_pin = DigitalInOut(board.D12)
        pn532 = PN532_I2C(i2c, debug=False, reset=reset_pin, req=req_pin)

        ic, ver, rev, support = pn532.firmware_version
        self.log.info("Found PN532 I2C with firmware version: {0}.{1}".format(ver, rev))

        # Configure PN532 to communicate with MiFare cards
        pn532.SAM_configuration()

        return pn532
