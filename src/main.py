import sys
import time

from lib.nfc_utils import NFCUtils

PN532 = NFCUtils().start_i2c()
UNLOCK_UIDS = [12345]

def main():
    print("[i] Waiting for RFID/NFC card...\n")
    sys.stdout.flush()
    while True:
        # Check if a card is available to read
        uid = PN532.read_passive_target(timeout=0.5)

        # Try again if no card is available.
        if uid is None:
            continue

        card_id = ""
        for id in uid:
            card_id += str(id)
        card_id = int(card_id)

        print("[i] Found card with UID:", card_id)
        sys.stdout.flush()

        if card_id in UNLOCK_UIDS:
            print("  [+] Successfully unlocked door!")
            sys.stdout.flush()
        else:
            print("  [-] Invalid access card!")
            sys.stdout.flush()

        time.sleep(3)

if __name__ == "__main__":
    main()
