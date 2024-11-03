# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
# Copyright 2024 Kevin Kiefer @Furzbart
# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
#  Python Module for communication with viControl heatings using the serial Optolink interface
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program. If not, see <http://www.gnu.org/licenses/>.
# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
from typing import Optional

class viCommand(bytearray):
    """Representation of a command. Object value is a bytearray of address and length."""

    def __init__(
            self,
            name:str,
            data_type:str,
            address:str,
            length:int,
            unit: Optional[str] = "",
            access_mode: Optional[str] = "R",
            measurement: Optional[str] = "",
            min_value: Optional[int] = 0,
            max_value: Optional[int] = 0
    ):
        """initialize object using the attributes of the chosen command."""

        try:
            self._name = name
        except:
            raise
        
        self._address = address
        self._value_bytes = length
        self._type = data_type
        self._unit = unit
        self._access_mode = access_mode
        self._measurement = measurement
        self.command_name = name

        # create bytearray representation
        b = bytes.fromhex(self._address) + self._value_bytes.to_bytes(1, 'big')
        super().__init__(b)

    @property
    def name(self) -> str:
        return self._name

    @property
    def type(self) -> str:
        return self._type
    
    @property
    def unit(self) -> str:
        return self._unit
    
    @property
    def access_mode(self) -> str:
        return self._access_mode
    
    @property
    def measurement(self) -> str:
        return self._measurement
    
    @property
    def address(self):
        return self._address
        
    def __repr__(self) -> str:
        return self._name

    def calc_response_length(self, mode='r') -> int:
        """Returns the number of bytes in the response."""
        # request_response:
        # 2 'address'
        # 1 'Anzahl der Bytes des Wertes'
        # x 'Wert'
        if mode.lower() == 'r':
            return 3 + self._value_bytes
        elif mode.lower() == 'rw':
            # in write mode the written values are not returned
            return 3
        else:
            return 3 + self._value_bytes
        
