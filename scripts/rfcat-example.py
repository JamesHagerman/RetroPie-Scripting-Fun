#!/usr/bin/python
import sys
from rflib import *

# The middle of the two Northern California, 70cm, experimental bands:
FREQ = 434200000 # (BW = 0.6MHz = 600kHz) 433.60+(434.80-433.60)/2
# FREQ = 438500000 # (BW = 0.05MHz = 50kHz) 438.45+(438.55-438.45)/2

PKTLEN = 1       # Set packet length
DRATE = 512
try:
    d = RfCat()
    d.setModeIDLE() # atlas used three different inflections in his talks...
    d.setFreq(FREQ)
    d.setMdmModulation(MOD_2FSK)
    d.setMdmDeviatn(4500)
    d.makePktFLEN(PKTLEN)
    d.setMdmDRate(DRATE)
    d.setMdmSyncMode(0) # disable syncword and preamble as this is not used
                        # by the remote.
    #d.setMaxPower()    # Pretty sure this turns on the TX amp...
    bytes = [0, 0x41, 0xff] # Data to send

    # It is WRONG to use setModeTX() right before calling RFxmit()! Doing so 
    # will reset a bunch of stuff and your packet will not come out right!
    # d.setModeTX()  # NONONO! Do not call this right before RFxmit!

    d.RFxmit("".join(map(chr, bytes)))

    # WITHOUT THIS YOU WILL GET USB TIMEOUTS!
    d.setModeIDLE()  # DO THIS OR GET USB TIMEOUTS!
except Exception, e: # Make sure things are sane...
    d.setModeIDLE()  # Probably a good idea here too... just in case
    sys.exit("Error %s" % str(e))

