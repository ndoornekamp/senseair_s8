# Introduction
Python module for reading CO2 concentration from a Senseair S8 sensor connected to a Raspberry Pi

# Installation
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