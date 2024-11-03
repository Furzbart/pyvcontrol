from .viCommand import viCommand
import logging
import json

_LOGGER = logging.getLogger(__name__)

class viCommandException(Exception):
    pass

class viCommandSet:

    def __init__(self, json_path) -> None:
        self._filepath = json_path
        self._cmds_json = json.load(open(json_path))
        #self._commands = {c["name"]:viCommand(**c) for c in self._cmds_json}
        self._commands = {c["name"]: viCommand(**{k: v for k, v in c.items() if k != "active"}) for c in self._cmds_json if c.get("active")}

    def get_command_set(self):
        return self._cmds_json

    def get_all_commands(self) -> dict:
        return self._commands
    
    def get_command(self, command_name) -> viCommand:
        return self._commands[command_name]
    
    def get_command_from_bytes(self, b: bytearray) -> viCommand:
        """Create command from address b given as byte, only the first two bytes of b are evaluated."""
        try:
            _LOGGER.debug(f'Convert {b.hex()} to command')
            command_name = next(key for key, value in COMMAND_SET.get_all_commands().items() if value.address.lower() == b[0:2].hex())
        except:
            raise viCommandException(f'No Command matching {b[0:2].hex()}')
        return COMMAND_SET.get_all_commands()[command_name]
        
# FIXME: Use "static" path for config file, currently depending from where it was started
COMMAND_SET = viCommandSet("viCommands.json")