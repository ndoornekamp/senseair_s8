# Introduction
Python module for reading CO2 concentration from a Senseair S8 sensor connected to a Raspberry Pi

# Connecting the Senseair S8 to your Raspberry Pi
Hook up the Senseair S8 to your Raspberry Pi using the following schematic: 

![Connection schematic](connection_schematic.png "Connection schematic")

Image source: http://co2meters.com/Documentation/AppNotes/AN168-S8-raspberry-pi-uart.pdf 

# Module installation
```
pip install senseair-s8
```

# Usage
As a module:
```
from senseair_s8 import SenseairS8

senseair_s8 = SenseairS8()    
print(senseair_s8.co2())
```

From the command line:
```
python -m senseair_s8
```

# Troubleshooting
- This module expects the sensor to be connected to port `/dev/ttyS0`. It was only tested using that port, but you can override this settings when initialising the sensor:
```
sensair_s8 = SenseairS8(port='/dev/ttyS0')
```
- Out of the box, `/dev/ttyS0` is disabled on a Raspberry Pi, resulting in a `permission denied`-error. You can enable it by:
    1. Run `sudo raspi config`
    2. Select 5 Interfacting options
    3. Select P6 Serial
    4. Select No for login console, Yes for serial port hardware
    5. OK, Finish, Reboot - Yes