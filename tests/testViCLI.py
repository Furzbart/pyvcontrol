
import logging
from pyvcontrol.viControl import viControl, VC_CONFIG
from pyvcontrol.viCommand import viCommand
from pyvcontrol.viData import viData

if __name__ == '__main__':
    _vc = viControl()
    _vc.initialize_communication()
    print("Welcome to janky ass ViCLI :)")
    while True:
        _address = input("Enter viCommand address: ")
        try:
            _length = int(input("Enter viCommand length (bits)"))
        except ValueError:
            print("Unable to parse length as int")
            continue
        _data_type = input("Enter viCommand data type (see docs)")

        _cmd = viCommand(data_type=_data_type, address=_address, length=_length, name="test-cmd")
        VC_CONFIG.cmds["CLI_Command"] = _cmd

        res = _vc.execute_command(vc=_cmd, access_mode='read')

        print(f'Result : {res.value}')



