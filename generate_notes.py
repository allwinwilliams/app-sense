# midi_pitch_matrix = [21, 23, 24, 26, 28, 29, 31,
#         33, 35, 36, 38, 40, 41, 43,
#         45, 47, 48, 50, 52, 53, 55,
#         57, 59, 60, 62, 64, 65, 67,
#         69, 71, 72, 74, 76, 77, 79,
#         81, 83, 84, 86, 88, 89, 91,
#         93, 95, 96]
import math

midi_pitch_matrix = [
        21, 23, 24, 26, 28, 29, 31,
        33, 35, 36, 38, 40, 41, 43,
        45, 47, 48, 50, 52, 53, 55,
        57, 59, 60, 62, 64, 65, 67,
        69, 71, 72, 74, 76, 77, 79,
        81, 83, 84, 86, 88, 89, 91,
        93, 95, 96]


def in_scale(pitch, scale = 0):
    return midi_pitch_matrix[round(pitch)] + scale

def gyroment(x, y, z, scale):
    print('------------***************')
    print('GYROMETER')
    print('Y--',str(y))
    value = y * (43 - 5) + 5
    print('VALUE--',str(value))
    value = round(value)
    pitch = in_scale(value, scale)
    print('PITCH--',str(pitch))
    print('------------*****************')
    velocity = 60
    return (pitch, velocity)


def accelerometer(x, y, z, scale):
    print('------------+++++++++++++++++')
    print('ACCELEROMETER')
    x = normalize(x)
    y = normalize(y)
    z = normalize(z)

    value = combine(x, y, z)
    value = normalize(value, 5, 42)
    print('VALUE--', str(value))
    pitch = in_scale(value, scale)
    print('PITCH--',str(pitch))
    print('------------++++++++++++++++')
    return pitch

def experiment(x, y, z, scale, name):

    if(name == 'linear_acceleration'):
        pitch = accelerometer(x, y, z, scale)
        velocity = calculate_velocity(x, y, z)

    if(name == 'game_rotation_vector'):
        pitch, velocity = gyroment(x, y, z, scale)

    print('PITCH::', str(pitch))
    print('VELOCITY::', str(velocity))

    return [{'pitch': pitch, 'velocity': velocity}]

def santoor(x, y, z, scale, name):
    time = 0.5
    if(name == 'linear_acceleration'):
        # pitch = accelerometer(x, y, z, scale)
        # velocity = calculate_velocity(x, y, z)
        time = math.sqrt(x*x + y*y + z*z)
        pass

    if(name == 'game_rotation_vector'):
        print('------------***************')
        print('GYROMETER')
        print('X--',str(x))
        value = x * x * (44 - 20) + 20
        print('VALUE--',str(value))
        value = round(value)
        pitch = in_scale(value, scale)
        print('PITCH--',str(pitch))
        print('------------*****************')
        velocity = 60

        print('PITCH::', str(pitch))
        print('VELOCITY::', str(velocity))

        return [{'pitch': pitch, 'velocity': velocity, 'time': time}]

    return

def process(data, type, scale = 0):

    x = data['x']
    y = data['y']
    z = data['z']
    name = data['name']

    if type == 'santoor':
        return santoor(x, y, z, scale, name)

    return experiment(x, y, z, scale, name)

def calculate_velocity(x, y, z):
    # value = combine(x, y, z)
    # return (80 * value)
    norm_x = normalize(x, max_value = 90, min_value = 25)
    norm_y = normalize(y, max_value = 90, min_value = 25)
    norm_z = normalize(z, max_value = 90, min_value = 25)
    velocity = combine(x, y, z)
    return velocity

def combine(x, y, z):
    return int(math.sqrt(x * x + y * y + z * z))

def normalize(value, max_value = 44, min_value = 10):
    # return abs(1/value)
    calculated_value = abs(value)
    calculated_value = calculated_value / (1 + calculated_value)
    calculated_value = calculated_value * (max_value - min_value) + min_value
    calculated_value = round(calculated_value)
    return calculated_value

def sensor_process(data):
    result = []

    acceleration = data['data']['accelerometer'];
    combined = combine(acceleration['x'], acceleration['y'], acceleration['z'])
    print("SENSOR  ******************************** ")
    print("ACCELERATION")
    print(combined)
    if combined > 18000:
        return 2

    if combined > 19000:
        return 1

    # gyroscope = data['data']['gyroscope'];
    # x = normalize(gyroscope['x'])
    # y = normalize(gyroscope['y'])
    # z = normalize(gyroscope['z'])
    # value = combine(x, y, z)
    # result.append({'pitch': value, 'velocity': velocity, 'time': 0.4})

    return 0
