from flask import Flask
from flask import request
import json
from generate_notes import process, sensor_process
from midi_connection import send_pitch
from play_sound import play


last_note = -1

app = Flask(__name__, static_url_path='')

@app.route('/hello')
def hello():
    return "hii..."

@app.route('/')
def sensor_arg():
    data = request.args
    print('-------------')
    print(request.args.json)
    values = {}
    values['x'] = float(request.args.get('x'))
    values['y'] = float(request.args.get('y'))
    values['z'] = float(request.args.get('z'))
    channel = int(request.args.get('channel'))
    print(values)
    notes_data = process(values)

    if(notes_data):
        last_note = send_pitch(notes_data, channel, last_note)

    send_pitch(notes_data, channel = channel)
    return str(notes_data) + str(channel)



@app.route('/', methods = ['POST'])
def sensor():
    global last_note
    # data = request.values.get("name")
    print("JSON::")
    print (request.is_json)
    json_data = request.get_json()
    print (json_data)

    values = {}
    values['name'] = json_data['name']
    values['x'] = float(json_data['x'])
    values['y'] = float(json_data['y'])
    values['z'] = float(json_data['z'])
    channel = int(json_data['channel'])
    scale = int(json_data['scale'])
    type = json_data['type']
    print(values)
    # scale =
    notes_data = process(values, type, scale)
    print(str(notes_data))

    if(notes_data):
        last_note = send_pitch(notes_data, channel, last_note, type = type)

    return str(notes_data) + str(channel)



@app.route('/sensor', methods = ['POST'])
def sensor_nodemcu():
    global last_note
    print("REQUEST::")
    json_data = request.get_json()
    print (json_data)
    sensor_enable = sensor_process(json_data)
    if sensor_enable > 0:
        play(sensor_enable)

    return "Ok"

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")
