from flask import Flask
from flask import request
import json
from generate_notes import process
from midi_connection import send_pitch

app = Flask(__name__)

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

    send_pitch(notes_data, channel = channel)
    return str(notes_data) + str(channel)



@app.route('/', methods = ['POST'])
def sensor():
    # data = request.values.get("name")
    print("JSON::")
    print (request.is_json)
    json_data = request.get_json()
    print (json_data)

    values = {}
    values['x'] = float(json_data['x'])
    values['y'] = float(json_data['y'])
    values['z'] = float(json_data['z'])
    channel = int(json_data['channel'])
    print(values)

    notes_data = process(values)
    print(str(notes_data))

    send_pitch(notes_data, channel = channel)

    return str(notes_data) + str(channel)

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")
