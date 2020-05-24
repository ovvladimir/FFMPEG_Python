import subprocess
from microfone import MICROFONE

cmd = \
    f'ffmpeg -re -rtbufsize 100M -f dshow -i "video=1.3M WebCam:audio={MICROFONE}" ' \
    '-vcodec libx264 -b:v 8000k -vf "scale=w=trunc(oh*a/2)*2:h=720" ' \
    '-acodec ac3 -ac 2 -ab 128K -ar 44100 ' \
    '-f mpegts udp://127.0.0.1:1234'

try:
    subprocess.run(cmd)
except BaseException as e:
    print(e)
# CTRL + C - остановить
'ffplay udp://127.0.0.1:1234'
