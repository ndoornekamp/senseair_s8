import time
import serial


class SenseairS8:
    def __init__(self, port="/dev/ttyS0", baudrate=9600, timeout=0.5):
        self.ser = serial.Serial(port, baudrate=baudrate, timeout=timeout)
        self.ser.flushInput()

    def co2(self)
        """
        Returns the measured CO2 value in parts per million (ppm), or None in case of an exception.
        :rtype: int | None
        """
        try:
            self.ser.flushInput()
            self.ser.write(b"\xFE\x04\x00\x03\x00\x01\xd5\xc5")
            time.sleep(1)
            response = self.ser.read(7)

            high = response[3]
            low = response[4]
            co2 = (high * 256) + low
        except Exception as e:
            co2 = None
            print(e)

        return co2
