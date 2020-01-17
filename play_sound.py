import vlc
import time

# national = vlc.MediaPlayer("./sounds/sare-inst.mp3")
# national.play()

def play(sensor_value):
    if(sensor_value == 0):
        return

    print("Playing...")
    if(sensor_value == 1):
        print("soft")
        # national.stop()
        p = vlc.MediaPlayer("./sounds/lathi.mp3")
        p.play()

    if(sensor_value == 2):
        print("hard")
        # national.stop()
        p = vlc.MediaPlayer("./sounds/lathi.mp3")
        p.play()

    time.sleep(10)

    p.stop()
    # national.play()
    return
