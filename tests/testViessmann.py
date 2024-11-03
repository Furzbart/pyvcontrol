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

# Tests the connection to Viessmann. Needs a physical connection

import unittest
import logging
from pyvcontrol.viControl import viControl
from pyvcontrol.viCommand import viCommand


class MyTestCase(unittest.TestCase):
    def test_readsequence(self):
        vo = viControl()
        vo.initialize_communication()

        for cmd in viCommand.command_set.keys():
            if cmd != 'Energiebilanz':
                vd = vo.execute_read_command(cmd)
                print(f'{cmd} : {vd.value} {vd.unit}')

    def test_readonly(self):
        pass

if __name__ == '__main__':
    logging.basicConfig(filename='testViessmann.log', filemode='w', level=logging.DEBUG)
    unittest.main()
