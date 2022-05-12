# Setup 🔨

This section will explain the steps needed to setup a Raspberry Pi (4) as an NFC/RFID reader for access to **The Lab**

## Hardware ⚙️

The actual NFC/RFID reader used for this project will be linked in multiple ways below for preservation:

- [Amazon Link](https://www.amazon.com/gp/product/B01I1J17LC/)
- [Official Site](http://www.hiletgo.com/ProductDetail/2156958.html)
- Name: PN532 NFC NXP RFID Module V3
- Brand Name: HiLetgo
- Connectivity Technology: I2C
- Model Number: 3-01-1147
- Part Number: 3-01-1147
- UNSPSC Code: 44000000

## Wire it up 🔌

First, wire the Raspberry Pi up to your NFC/RFID reader:

![connected](assets/connected.jpg)

![setup-and-pins](assets/setup-and-pins.png)

> [setup source](https://blog.stigok.com/2017/10/12/setting-up-a-pn532-nfc-module-on-a-raspberry-pi-using-i2c.html)

![pinout-detailed](assets/pinout-detailed.png)

> [pinout source](https://pinout.xyz/pinout/i2c)

Ensure that your NFC/RFID reader is in I2C mode:

| off | on |
|-----|----|
|     | x  |
| x   |    |

### System 📦

The only packages you will need on your system (Raspberry Pi) are the following:

- Docker
- Make
- docker-compose

### Code 💻

To learn more about the circuit python package which is the underlying code for the NFC/RFID reader, visit the following link:

[adafruit-pn532-rfid-nfc docs](https://learn.adafruit.com/adafruit-pn532-rfid-nfc/python-circuitpython)
