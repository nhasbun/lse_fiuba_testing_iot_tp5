"""
Communication test module for insytech compass subsystem.

List of requirements:
* CompassModbus wrapper class with port and slave address
* CompassModbus minimalmodbus usage
* CompassModbus start communication via init method
* is_valid_hw false for wrong HW ID
* is_valid_hw true for right HW ID
* is_valid_version false for wrong VERSION ID
* is valid_version true for right VERSION ID
"""

import unittest
from unittest.mock import Mock
from unittest.mock import patch

from compass_middleware.compass_modbus import CompassModbus, Instrument
from minimalmodbus import Instrument as LibraryInstrument


class TestCompassModbus(unittest.TestCase):

    def test_constructor_with_port_address(self):
        """
        Correct storage of modbus port and instrument slave address
        """
        desired_port = "COM2"
        desired_add = 0xFF

        new_compass_com = CompassModbus(port=desired_port, address=desired_add)

        obj_port = new_compass_com.get_port()
        obj_address = new_compass_com.get_address()

        self.assertEqual((desired_port, desired_add), (obj_port, obj_address))

    def test_minimalmodbus_instrument_usage(self):
        """
        Checking correct method resolution order (minimalmodbus requirement)
        """
        mro_library = LibraryInstrument.mro()
        mro_wrapper = Instrument.mro()
        self.assertEqual(mro_library[0], mro_wrapper[0])

    @patch('compass_middleware.compass_modbus.Instrument')
    def test_minimalmodbus_api_initialization(self, instrument_t_mock):
        """
        Initialization of minimalmodbus instrument with port and address
        """
        instrument_instance = Mock()
        instrument_t_mock.return_value = instrument_instance

        new_compass_com = CompassModbus(port="", address=0xFF)
        new_compass_com.init()

        instrument_t_mock.assert_called_once_with("", 0xFF)

    @patch('compass_middleware.compass_modbus.Instrument')
    def test_hw_id_wrong(self, instrument_t_mock):
        """
        No valid hardware if code on register not correct
        """
        def fake_read_register(reg):
            if reg == 0x00:
                return 0x22  # injecting wrong code
            else:
                return 0xFF

        instrument_t_mock().read_register.side_effect = fake_read_register

        new_compass_com = CompassModbus(port="", address=0xFF)
        new_compass_com.init()
        self.assertFalse(new_compass_com.is_valid_hw())

    @patch('compass_middleware.compass_modbus.Instrument')
    def test_hw_id_right(self, instrument_t_mock):
        """
        Valid HW detected on right code
        """

        def fake_read_register(reg):
            if reg == 0x00:
                return 0x24  # correct code
            else:
                return 0xFF

        instrument_t_mock().read_register.side_effect = fake_read_register

        new_compass_com = CompassModbus(port="", address=0xFF)
        new_compass_com.init()
        self.assertTrue(new_compass_com.is_valid_hw())

    @patch('compass_middleware.compass_modbus.Instrument')
    def test_version_id_wrong(self, instrument_t_mock):
        """
        No valid version if code on register not correct
        """

        def fake_read_register(reg):
            if reg == 0x01:
                return 0xFF  # injecting wrong code
            else:
                return 0xFF

        instrument_t_mock().read_register.side_effect = fake_read_register

        new_compass_com = CompassModbus(port="", address=0xFF)
        new_compass_com.init()
        self.assertFalse(new_compass_com.is_valid_version())

    @patch('compass_middleware.compass_modbus.Instrument')
    def test_version_id_right(self, instrument_t_mock):
        """
        Valid version detected on right code
        """

        def fake_read_register(reg):
            if reg == 0x01:
                return 0x01  # injecting wrong code
            else:
                return 0xFF

        instrument_t_mock().read_register.side_effect = fake_read_register

        new_compass_com = CompassModbus(port="", address=0xFF)
        new_compass_com.init()
        self.assertTrue(new_compass_com.is_valid_version())




if __name__ == '__main__':
    unittest.main()
