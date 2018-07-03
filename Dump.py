#!/usr/bin/env python3
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while True:
  try:
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
      print("Card detected")
    
    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:

      # Print UID
      print("Card read UID:{:>4}{:>4}{:>4}{:>4}".format(*uid))
  
      # This is the default key for authentication
      key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
      
      # Select the scanned tag
      MIFAREReader.MFRC522_SelectTag(uid)

      # Dump the data
      MIFAREReader.MFRC522_DumpClassic1K(key, uid)

      # Stop
      MIFAREReader.MFRC522_StopCrypto1()

  except KeyboardInterrupt:
    print("\nCtrl+C captured, ending read.")
    break

GPIO.cleanup()