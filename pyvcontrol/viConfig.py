# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
# Copyright 2024 Kevin Kiefer
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

'''Configuration class for viControl'''
from .viCommand import viCommand
import logging, json, os

_LOGGER = logging.getLogger(__name__)

class viCommandException(Exception):
    pass

class viConfig:
    def __init__(self) -> None:
        _config_dir = os.path.join(os.path.dirname(__file__), '../config')
        _cmds_path = os.path.join(_config_dir, 'viCommands.json')
        _config_path = os.path.join(_config_dir, 'viConfig.json')

        self._cmds_json = json.load(open(_cmds_path, 'r'))
        self._commands = {c["name"]: viCommand(**{k: v for k, v in c.items() if k != "active"}) for c in self._cmds_json if c.get("active")}
        self._config = json.load(open(_config_path, 'r'))

    def get_command_set(self):
        return self._cmds_json

    def get_commands(self) -> dict:
        return self._commands
    
    def get_command(self, command_name) -> viCommand:
        return self._commands[command_name]
    
    def get_command_from_bytes(self, b: bytearray) -> viCommand:
        """Create command from address b given as byte, only the first two bytes of b are evaluated."""
        try:
            _LOGGER.debug(f'Convert {b.hex()} to command')
            command_name = next(key for key, value in self.get_commands().items() if value.address.lower() == b[0:2].hex())
        except:
            raise viCommandException(f'No Command matching {b[0:2].hex()}')
        return self.get_commands()[command_name]
    
    def get_config(self):
        return self._config
    
    def get_device(self) -> str:
        return self._config['optolink_device']
    
    def get_api_port(self) -> str:
        return self._config['api_port']
    
    def get_api_basepath(self) -> str:
        return self._config['api_basepath']
    
    def get_api_host(self) -> str:
        return self._config['api_host']
        
VC_CONFIG = viConfig()