import subprocess
from microfone import MICROFONE

cmd =                                                      \
    'ffmpeg -y -loglevel error -f dshow -rtbufsize 1000M ' \
    f'-i "video=1.3M WebCam:audio={MICROFONE}" '           \
    '-vf scale=640:480 -vcodec libx264 -preset ultrafast ' \
    '-vf format=yuv420p test.mp4'
try:
    subprocess.run(cmd)
except BaseException as e:
    print(e)
# CTRL + C - остановить
