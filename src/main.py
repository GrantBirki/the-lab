import time

import board
import busio
from adafruit_pn532.i2c import PN532_I2C
from digitalio import DigitalInOut

UNLOCK_UIDS = [12345]

# I2C connection:
i2c = busio.I2C(board.SCL, board.SDA)

reset_pin = DigitalInOut(board.D6)
req_pin = DigitalInOut(board.D12)
pn532 = PN532_I2C(i2c, debug=False, reset=reset_pin, req=req_pin)

ic, ver, rev, support = pn532.firmware_version
print("[i] Found PN532 with firmware version: {0}.{1}".format(ver, rev))

# Configure PN532 to communicate with MiFare cards
pn532.SAM_configuration()

print("[i] Waiting for RFID/NFC card...\n")
while True:
    # Check if a card is available to read
    uid = pn532.read_passive_target(timeout=0.5)

    # Try again if no card is available.
    if uid is None:
        continue

    card_id = ""
    for id in uid:
        card_id += str(id)
    card_id = int(card_id)

    print("[i] Found card with UID:", card_id)

    if card_id in UNLOCK_UIDS:
        print("  [+] Successfully unlocked door!")
    else:
        print("  [-] Invalid access card!")

    time.sleep(3)
