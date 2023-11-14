import time

from senseair_s8 import SenseairS8


senseair_s8 = SenseairS8()
while True:
    co2 = senseair_s8.co2()
    print(co2)
    time.sleep(1)
