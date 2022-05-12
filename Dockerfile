FROM python:3.10.4-slim-buster

# Pin the version of libnfc to use
ENV LIBNFC_VERSION=1.8.0

# Use BASH shell
SHELL ["/bin/bash", "-c"]

# Install dependencies
RUN apt-get update
RUN apt-get -y install wget zip gcc autoconf automake libtool pkg-config make usbutils i2c-tools

# Install libnfc
RUN wget https://github.com/nfc-tools/libnfc/archive/libnfc-$LIBNFC_VERSION.tar.gz
RUN tar -xvzf libnfc-$LIBNFC_VERSION.tar.gz
RUN sh -c "echo /usr/local/lib > /etc/ld.so.conf.d/usr-local-lib.conf"
RUN ldconfig
RUN mkdir -p /etc/nfc/devices.d
WORKDIR /libnfc-libnfc-$LIBNFC_VERSION
RUN autoreconf -vis
RUN ./configure --with-drivers=pn532_i2c --enable-debug --prefix=/usr --sysconfdir=/etc
RUN make clean
RUN make
RUN make install

# Set NFC device to I2C
RUN echo -e 'device.name = "PN532 over I2C"\ndevice.connstring = "pn532_i2c:/dev/i2c-1"' >> /etc/nfc/libnfc.conf

WORKDIR /app
ENTRYPOINT ["/bin/bash"]
