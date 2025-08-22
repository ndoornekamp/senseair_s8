import time

from senseair_s8 import SenseairS8
from senseair_s8.senseair_s8 import SenseairS8Exception

senseair_s8 = SenseairS8()
while True:
    try:
        co2 = senseair_s8.co2()
        print(co2)
    except SenseairS8Exception as e:
        print(f"Error reading CO2 value: {e}")

    time.sleep(1)
