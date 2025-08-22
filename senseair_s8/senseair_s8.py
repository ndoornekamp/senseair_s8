import time
import serial


class SenseairS8Exception(Exception):
    pass


class SenseairS8:
    """
    Interface for the Senseair S8 CO2 sensor over a serial connection.

    This class allows you to communicate with a Senseair S8 sensor to read CO2 concentration values in ppm.

    Example usage:

        from senseair_s8 import SenseairS8
        sensor = SenseairS8()
        co2 = sensor.co2()
        print(f"CO2 concentration: {co2} ppm")

    Args:
        port (str): Serial port device (default: "/dev/ttyS0").
        baudrate (int): Serial baudrate (default: 9600).
        timeout (float): Serial timeout in seconds (default: 0.5).
    """

    def __init__(self, port="/dev/ttyS0", baudrate=9600, timeout=0.5):
        self.ser = serial.Serial(port, baudrate=baudrate, timeout=timeout)
        self.ser.flushInput()

    def co2(self) -> int:
        """
        Returns the measured CO2 value in parts per million (ppm).

        Returns:
            int: The CO2 concentration in ppm.

        Raises:
            SenseairS8Exception: If reading from the sensor fails.
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
            raise SenseairS8Exception("Failed to read CO2 value") from e

        return co2
