import mido
import time

outport = mido.open_output('IAC Driver allwin_iac_bus')

def send_midi(notes, port = outport, delay = 0):
    for note in notes:
        print(note)
        port.send(note)
        time.sleep(0.5)

def generate_message(note = 60, velocity = 80, time = 0, channel = 1):
    return [
            mido.Message('note_on', channel = channel, note = note, velocity = velocity, time = 0),
            mido.Message('note_off', channel = channel, note = note, velocity = velocity, time = 0)
            ]

def send_pitch(notes, channel = 1):
    print(notes)
    print(channel)
    for note in notes:
        send_midi(generate_message(channel = channel, note = note['pitch'], velocity = note['velocity']))

    return "success"

send_midi(generate_message(60, 60, 1, channel = 2), outport, delay = 1000)

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
