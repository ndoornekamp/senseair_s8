import time
import serial


class SenseairS8:
    
    def __init__(self, port="/dev/ttyS0", baudrate=9600, timeout=.5):
        self.ser = serial.Serial(port, baudrate=baudrate, timeout=timeout)
        self.ser.flushInput()
    
    def co2(self):
        try:
            self.ser.flushInput()
            self.ser.write(b"\xFE\x44\x00\x08\x02\x9F\x25")
            time.sleep(1)
            response = self.ser.read(7)

            high = response[3]
            low = response[4]
            co2 = (high*256) + low
        except Exception as e:
            co2 = None
            print(e)
        
        return co2
    
if __name__ == "__main__":
    senseair_s8 = SenseairS8()
    
    print(senseair_s8.co2())