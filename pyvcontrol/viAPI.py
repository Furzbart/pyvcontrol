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

'''REST API using python flask for pyViControl'''

from flask import Flask, jsonify
from pyvcontrol.viControl import viControl
from pyvcontrol.viConfig import VC_CONFIG

app = Flask(__name__)
basepath = VC_CONFIG.get_api_basepath()

error_cmd_not_found = {
    'message': 'Command not found!',
    'status': 'error',
    'http_code': 404
}

@app.route(f'{basepath}status', methods=['GET'])
def get_status():
    try:
        vo = viControl()
        vo.initialize_communication()
        return jsonify({'message':'Connectiviy test successful', 'status': 'success'}), 200
    except:
        return jsonify({'message':'No connection to viessmann device', 'status': 'error'}), 503


@app.route(f'{basepath}commands/all', methods=['GET'])
def get_all_commands():
    try:
        vo = viControl()
        vo.initialize_communication()

        reponse_json = {}
        for cmd in VC_CONFIG.get_commands().keys():
                if cmd != 'Energiebilanz':
                    vd = vo.execute_read_command(cmd)
                    reponse_json[cmd] = {
                	'command':cmd,
               	 	'raw':vd.value,
                	'unit':vd.unit,
                	'value':f'{vd.value}{vd.unit}'
                    }
        return jsonify(reponse_json), 200
    except Exception as ex:
        return jsonify({'message':'No connection to viessmann device', 'status': 'error', 'exception': ex.__str__}), 503

@app.route(f'{basepath}commands', methods=['GET'])
def get_command_list():
    return jsonify(VC_CONFIG.get_command_set()), 200


@app.route(f'{basepath}command/<command>', methods=['GET'])
def get_command(command):
    try:
        if not command in VC_CONFIG.get_commands().keys():
            return jsonify(error_cmd_not_found), 404
        vo = viControl()
        vo.initialize_communication()
        vd = vo.execute_read_command(command_name=command)
        response = {
            'command':command,
            'value':f'{vd.value}{vd.unit}',
            'unit':vd.unit,
            'raw':vd.value
        }
        return jsonify(response), 200
    except:
        return jsonify({'message':'No connection to viessmann device', 'status': 'error'}), 503


if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host=VC_CONFIG.get_api_host(), port=VC_CONFIG.get_api_port())