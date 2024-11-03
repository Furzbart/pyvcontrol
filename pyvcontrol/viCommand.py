# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
# Copyright 2021 Jochen Schmähling
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


import logging

ACCESS_MODE = 'access_mode'
TYPE = 'type'
UNIT = 'unit'
LENGTH = 'length'
ADDRESS = 'address'


VITOCAL_V200A = {
    # All Parameters are tested and working on Vitocal 200A 204C

    # ------ Statusinfos (read only) ------

    # Aussentemperatur (-40..70)
    'Aussentemperatur': {ADDRESS: '0101', LENGTH: 2, TYPE: 'IS10', UNIT: '°C'},

    # Warmwasser: Warmwassertemperatur oben (0..95) - Immer verfügbar
    'WWTemperatur_oben': {ADDRESS: '010d', LENGTH: 2, TYPE: 'IS10', UNIT: '°C'},

    # Warmwasser: Warmwassertemperatur unten (0..95) - Nur bei mehreren Sensoren, ansonsten 0
    #'WWTemperatur_unten': {ADDRESS: '010e', LENGTH: 2, UNIT: 'IS10', UNIT: '°C'},

    # Warmwasser: Warmwassertemperatur mitte (0..95) - Nur bei mehreren Sensoren, ansonsten 0
    #'WWTemperatur_mitte': {ADDRESS: '010f', LENGTH: 2, UNIT: 'IS10', UNIT: '°C'},

    # Warmwasser: Warmwassertemperatur Solltemperatur (0..95)
    'WWSollTemperatur': {ADDRESS: '6000', LENGTH: 2, TYPE: 'IS10', UNIT: '°C'},

    # Vorlauftemp Soll HK1
    'VorlauftempSollHK1': {ADDRESS: '1800', LENGTH: 2, TYPE: 'IS10', UNIT: '°C'},

    # Heizkreis HK1: Vorlauftemperatur Sekundaer 1 (0..95)
    'VorlauftempSek': {ADDRESS: '0105', LENGTH: 2, TYPE: 'IS10', UNIT: '°C'},

    # Heizkreis HK1: Ruecklauftemperatur Sekundaer  (0..95)
    'RuecklauftempSek': {ADDRESS: '0106', LENGTH: 2, TYPE: 'IS10', UNIT: '°C'},

    # Sekundaerpumpe [%] (including one status byte)
    'Sekundaerpumpe': {ADDRESS: 'B421', LENGTH: 2, TYPE: 'IUNON', UNIT: '%'},

    # Vorlauftemperatur Primaer 1 (0..95)
    'VorlauftempPrim': {ADDRESS: '0103', LENGTH: 2, TYPE: 'IS10', UNIT: '°C'},

    # Ruecklauftemperatur Primaer (0..95)
    'RuecklauftempPrim': {ADDRESS: '0104', LENGTH: 2, TYPE: 'IS10', UNIT: '°C'},

    # Faktor Energiebilanz(1 = 0.1kWh, 10 = 1kWh, 100 = 10kWh)
    'FaktorEnergiebilanz': {ADDRESS: '163F', LENGTH: 1, TYPE: 'IUNON', UNIT: ''},

    # Heizwärme  "Heizbetrieb", Verdichter 1
    'Heizwaerme': {ADDRESS: '1640', LENGTH: 4, TYPE: 'IUNON', UNIT: 'kWh'},

    # Elektroenergie "Heizbetrieb", Verdichter 1
    'Heizenergie': {ADDRESS: '1660', LENGTH: 4, TYPE: 'IUNON', UNIT: 'kWh'},

    # Heizwärme  "WW-Betrieb", Verdichter 1
    'WWwaerme12M': {ADDRESS: '1650', LENGTH: 4, TYPE: 'IUNON', UNIT: 'kWh'},

    # Elektroenergie "WW-Betrieb", Verdichter 1
    'WWenergie12M': {ADDRESS: '1670', LENGTH: 4, TYPE: 'IUNON', UNIT: 'kWh'},

    # Primaerquelle [%] (including one status byte)
    'Primaerquelle': {ADDRESS: 'B420', LENGTH: 2, TYPE: 'IUNON', UNIT: '%'},

    # Warmwasserpumpe [%] (including one status byte)
    'Warmwasserpumpe': {ADDRESS: 'B422', LENGTH: 2, TYPE: 'IUNON', UNIT: '%'},

    # Verdichter [%] (including one status byte)
    'Verdichter': {ADDRESS: 'B423', LENGTH: 4, TYPE: 'IUNON', UNIT: '%'},

    # Lüfterdrehzahl
    'LuefterGeschw': {ADDRESS: '1A53', LENGTH: 1, TYPE: 'IUNON', UNIT: 'u/min'},

    # Verdichterdrehzahl
    'VerdichterGeschw': {ADDRESS: '1A54', LENGTH: 1, TYPE: 'IUNON', UNIT: '%'},

    # Lüfterdrehzahl
    'LuefterGeschw2': {ADDRESS: '1A52', LENGTH: 1, TYPE: 'IUNON', UNIT: 'u/min'},

    # Druck Sauggas [bar] (including one status byte) - Kühlmittel
    'DruckSauggas': {ADDRESS: 'B410', LENGTH: 3, TYPE: 'IS10', UNIT: 'bar'},

    # Druck Heissgas [bar] (including one status byte)- Kühlmittel
    'DruckHeissgas': {ADDRESS: 'B411', LENGTH: 3, TYPE: 'IS10', UNIT: 'bar'},

    # Temperatur Sauggas [°C] (including one status byte)- Kühlmittel
    'TempSauggas': {ADDRESS: 'B409', LENGTH: 3, TYPE: 'IS10', UNIT: '°C'},

    # Temperatur Heissgas [°C] (including one status byte)- Kühlmittel
    'TempHeissgas': {ADDRESS: 'B40A', LENGTH: 3, TYPE: 'IS10', UNIT: '°C'},

    # JAZ
    'Jahresarbeitszahl': {ADDRESS: '1680', LENGTH: 1, TYPE: 'IS10', UNIT: ''},

    # JAZ Nur Heizen
    'JahresarbeitszahlHeizen': {ADDRESS: '1681', LENGTH: 1, TYPE: 'IS10', UNIT: ''},

    # JAZ Nur Warmwasser
    'JahresarbeitszahlWW': {ADDRESS: '1682', LENGTH: 1, TYPE: 'IS10', UNIT: ''},

    # --------- Menüebene -------

    # Betriebsmodus
    'Betriebsmodus': {ADDRESS: 'B000', LENGTH: 1, TYPE: 'BA', ACCESS_MODE: 'write', UNIT: ''},

    # getManuell / setManuell -- 0 = normal, 1 = manueller Heizbetrieb, 2 = 1x Warmwasser auf Temp2
    'WWeinmal': {ADDRESS: 'B020', LENGTH: 1, TYPE: 'OO', ACCESS_MODE: 'write', UNIT: ''},

    # Warmwassersolltemperatur (10..60 (95))
    'SolltempWarmwasser': {ADDRESS: '6000', LENGTH: 2, TYPE: 'IS10', ACCESS_MODE: 'write', 'min_value': 10,
                           'max_value': 60, UNIT: '°C'},

    # Raumtemp Soll HK1
    'RaumtempSollHK1': {ADDRESS: '2000', LENGTH: 2, TYPE: 'IS10', UNIT: '°C'},

    # Heizkennlinie Neigung
    'HKLNeigung': {ADDRESS: '2007', LENGTH: 2, TYPE: 'IS10', UNIT: ''},

    # Hiezkennlinie Niveau
    'HKLNiveau': {ADDRESS: '2006', LENGTH: 2, TYPE: 'IS10', UNIT: '°C'},

    # --------- Codierebene 2 ---------

    # Hysterese Vorlauf ein: Verdichter schaltet im Heizbetrieb ein
    'Hysterese_Vorlauf_lowerLimit': {ADDRESS: '7304', LENGTH: 2, TYPE: 'IU10', ACCESS_MODE: 'write', UNIT: '°C'},

    # Hysterese Vorlauf aus: Verdichter schaltet im Heizbetrieb ab
    'Hysterese_Vorlauf_upperLimit': {ADDRESS: '7313', LENGTH: 2, TYPE: 'IU10', ACCESS_MODE: 'write', UNIT: '°C'},

    # --------- Function Call --------
    # Funktioniert nicht - ???
    #'Energiebilanz': {ADDRESS: 'B800', LENGTH: 16, TYPE: 'F_E', ACCESS_MODE: 'call'},

}


class viCommandException(Exception):
    pass


class viCommand(bytearray):
    """Representation of a command. Object value is a bytearray of address and length."""

    # =============================================================
    # CHANGE YOUR COMMAND SET HERE:
    command_set = VITOCAL_V200A

    # =============================================================

    def __init__(self, command_name):
        """initialize object using the attributes of the chosen command."""

        try:
            command = self.command_set[command_name]
        except:
            raise viCommandException(f'Unknown command {command_name}')
        self._command_code = command[ADDRESS]
        self._value_bytes = command[LENGTH]
        self.type = command[TYPE]
        self.unit = command[UNIT]
        self.access_mode = self._get_access_mode(command)
        self.command_name = command_name
        # create bytearray representation
        b = bytes.fromhex(self._command_code) + self._value_bytes.to_bytes(1, 'big')
        super().__init__(b)

    def _get_access_mode(self, command):
        if ACCESS_MODE in command.keys():
            return command[ACCESS_MODE]
        else:
            return 'read'

    @classmethod
    def _from_bytes(cls, b: bytearray):
        """Create command from address b given as byte, only the first two bytes of b are evaluated."""
        try:
            logging.debug(f'Convert {b.hex()} to command')
            command_name = next(key for key, value in cls.command_set.items() if value[ADDRESS].lower() == b[0:2].hex())
        except:
            raise viCommandException(f'No Command matching {b[0:2].hex()}')
        return viCommand(command_name)

    def response_length(self, access_mode='read'):
        """Returns the number of bytes in the response."""
        # request_response:
        # 2 'address'
        # 1 'Anzahl der Bytes des Wertes'
        # x 'Wert'
        if access_mode.lower() == 'read':
            return 3 + self._value_bytes
        elif access_mode.lower() == 'write':
            # in write mode the written values are not returned
            return 3
        else:
            return 3 + self._value_bytes
