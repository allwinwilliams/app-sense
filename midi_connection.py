import mido
import time

outport = { 'default': mido.open_output('IAC Driver allwin_iac_bus'),
            'sensors': mido.open_output('IAC Driver sensors_iac'),
            'santoor': mido.open_output('IAC Driver santoor_iac'),
            'pad': mido.open_output('IAC Driver pad_iac'),
            'piano': mido.open_output('IAC Driver piano_iac'),
            'strings': mido.open_output('IAC Driver strings_iac'),
            'drums': mido.open_output('IAC Driver drums_iac')
            }


def send_midi(notes, port = outport['default'], delay = 0.5):
    for note in notes:
        print(note)
        port.send(note)
        print("delay------------------------------------>>>>>>>>>>>>>>>")
        print(delay)
        time.sleep(0.5)


def generate_message(note = 60, velocity = 80, time = 0, channel = 1):
    return [
            mido.Message('note_on', channel = channel, note = note, velocity = velocity, time = 0),
            mido.Message('note_off', channel = channel, note = note, velocity = velocity, time = 0)
            ]

def send_pitch(notes, channel = 1, last_pitch = 0, type = 'pad'):
    print(notes)
    print(channel)
    for note in notes:
        print('LAST NOTE')
        print(last_pitch)
        delay = 0.5
        if('time' in note):
            delay = note['time']

        if(last_pitch != note['pitch']):
            last_pitch = note['pitch']
            # send_midi(generate_message(channel = channel, note = note['pitch'], velocity = note['velocity']), port = outport[type])
            send_midi(generate_message(channel = channel, note = note['pitch'], velocity = note['velocity']))
            return last_pitch

    return last_pitch

# def get_ctl_msgs(param, value):
#         if param == 'BEND_RANGE':
#             return [
#                 mido.Message('control_change', channel=self.channel,
#                         control=101, value=0),
#                 mido.Message('control_change', channel=self.channel,
#                         control=100, value=0),
#                 mido.Message('control_change', channel=self.channel,
#                         control=6, value=value),
#                 mido.Message('control_change', channel=self.channel,
#                         control=38, value=0)
#             ]
#         else:
#             ctl = PARAM_CTL_MAPPING[param]['ctl']
#             val = PARAM_CTL_MAPPING[param]['map'](value)
#             return [mido.Message('control_change', channel=self.channel,
#                           control=ctl, value=val)]
