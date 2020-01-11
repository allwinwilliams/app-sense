# midi_pitch_matrix = [21, 23, 24, 26, 28, 29, 31,
#         33, 35, 36, 38, 40, 41, 43,
#         45, 47, 48, 50, 52, 53, 55,
#         57, 59, 60, 62, 64, 65, 67,
#         69, 71, 72, 74, 76, 77, 79,
#         81, 83, 84, 86, 88, 89, 91,
#         93, 95, 96]
from math import sqrt

midi_pitch_matrix = [21, 23, 24, 26, 28, 29, 31,
        33, 35, 36, 38, 40, 41, 43,
        45, 47, 48, 50, 52, 53, 55,
        57, 59, 60, 62, 64, 65, 67,
        69, 71, 72, 74, 76, 77, 79,
        81, 83, 84, 86, 88, 89, 91,
        93, 95, 96]

def in_scale(pitch, scale = 0):
    return midi_pitch_matrix[pitch + scale]

def process(data):
    x = normalize(data['x'])
    y = normalize(data['y'])
    z = normalize(data['z'])
    value = combine(x, y, z)
    pitch = in_scale(value)
    velocity = 50
    return [{'pitch': pitch, 'velocity': velocity}]


def combine(x, y, z):
    return int(sqrt(x * x + y * y + z * z))

def normalize(value, max_value = 45, min_value = 5):
    # return abs(1/value)
    calculated_value = abs(value)
    calculated_value = calculated_value / (1 + calculated_value)
    calculated_value = calculated_value * (max_value - min_value) + min_value
    calculated_value = round(calculated_value)
    return calculated_value
