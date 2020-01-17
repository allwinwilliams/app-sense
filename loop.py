import vlc
import time

while True:
    national = vlc.MediaPlayer("./sounds/sare-inst.mp3")
    national.play()
    time.sleep(50)
