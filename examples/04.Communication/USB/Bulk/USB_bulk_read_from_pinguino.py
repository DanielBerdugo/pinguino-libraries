#!/usr/bin/env python
# The initial program is from Yeison Cardona to test usb exchange with Pinguino V2.12
# Here it is modified to test usb exchange with Pinguino V4 - author A. Gentric

import usb
import time

VENDOR = 0x04D8
PRODUCT = 0xFEAA

TIMEOUT = 10000
INTERFACE = 0
ENDPOINT_OUT = 0x01

# if bootloader v4.x
CONFIGURATION = 0x01
ENDPOINT_IN = 0x81

# if bootloader v2.x
#CONFIGURATION = 0x03
#ENDPOINT_IN = 0x82

def read(dh, length, timeout = 0):
  return dh.bulkRead(ENDPOINT_IN, length, timeout)

def write(dh, buffer, timeout = 0):
  return dh.bulkWrite(0x01, buffer, timeout)

busses = usb.busses()

# Search pinguino between all the usb devices
for bus in busses:
  devices = bus.devices
  for dev in devices:
    if dev.idVendor==VENDOR and dev.idProduct==PRODUCT:
      pinguino = dev

# Get a device handler for the usb device
dh = pinguino.open()
dh.setConfiguration(CONFIGURATION)
dh.claimInterface(INTERFACE)

# receiving a message from Pinguino
while True :
  message = ""
  lu = None
  while lu==None :
    try :
      lu=dh.bulkRead (ENDPOINT_IN, 64, TIMEOUT)
    except usb.USBError as err:
      pass
  for i in lu:
    message += chr(i)
  print message

"""
tempo=1
while True: 
  cadena = ""
  lu= None
  time.sleep(tempo)
# receiving data one character at a time from Pinguino
  while lu==None :
    try :
      lu=dh.bulkRead (ENDPOINT_IN, 1, TIMEOUT)
    except usb.USBError as err:
      pass
  for i in lu:
    cadena += chr(i)
  print cadena
"""
