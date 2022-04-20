"""
Packaging compass modbus communication into a single module
"""
from typing import Union

from minimalmodbus import Instrument


class CompassModbus:

    def __init__(self, port, address):
        self._compass = None
        self._port = port
        self._add = address

    def get_port(self):
        return self._port

    def get_address(self):
        return self._add

    def init(self):
        self._compass = Instrument(self._port, self._add)

    def is_valid_hw(self):
        hw_id = self._compass.read_register(0x00)
        return hw_id == 0x24

    def is_valid_version(self):
        version_id = self._compass.read_register(0x01)
        return version_id == 0x01
