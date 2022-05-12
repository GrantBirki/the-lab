import logging
import sys

from lib.nfc_utils import NFCUtils

LOG = logging.getLogger('logger')
LOG.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
NFC = NFCUtils(LOG)

def main():
    print("[i] Waiting for RFID/NFC card...\n")
    sys.stdout.flush()
    while True:
        # Check if a card is available to read
        uid = NFC.scan()

        # Try again if no card is available.
        if uid is None:
            continue

        # Do whatever you want with the card's UID here!
        # Unlock doors, activate lights, etc

if __name__ == "__main__":
    main()
