from unittest.mock import MagicMock, patch

import pytest

from senseair_s8.senseair_s8 import SenseairS8, SenseairS8Exception


@patch("serial.Serial")
def test_init_opens_serial(mock_serial: MagicMock) -> None:
    SenseairS8(port="/dev/some-non-default-port", baudrate=19200, timeout=1.0)
    mock_serial.assert_called_once_with("/dev/some-non-default-port", baudrate=19200, timeout=1.0)


@patch("serial.Serial")
def test_co2_reads_value(mock_serial: MagicMock) -> None:
    mock_ser = MagicMock()
    # Simulate a valid 7-byte response: [.., .., .., high, low, .., ..]
    mock_ser.read.return_value = b"\x00\x00\x00\x01\xf4\x00\x00"  # 0x01f4 --> 500 ppm
    mock_serial.return_value = mock_ser

    s8 = SenseairS8()
    value = s8.co2()

    assert value == 500
    mock_ser.write.assert_called_once_with(b"\xfe\x04\x00\x03\x00\x01\xd5\xc5")
    mock_ser.reset_input_buffer.assert_called_once()


@patch("serial.Serial")
def test_co2_raises_on_exception(mock_serial: MagicMock) -> None:
    mock_ser = MagicMock()
    mock_ser.read.side_effect = Exception("serial error")
    mock_serial.return_value = mock_ser

    s8 = SenseairS8()

    with pytest.raises(SenseairS8Exception):
        s8.co2()
