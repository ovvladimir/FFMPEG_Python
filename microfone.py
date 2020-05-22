# http://wiki.rosalab.ru/ru/index.php/FFmpeg
# https://help.ubuntu.ru/wiki/ffmpeg
import subprocess

devices = subprocess.run(
    # список оборудования
    'ffmpeg -list_devices true -f dshow -i dummy',
    stderr=subprocess.PIPE, encoding='utf-8').stderr

mic = False
if devices.find('Микрофон') != -1:
    mic = 'Микрофон'
elif devices.find('Microfone') != -1:
    mic = 'Microfone'
if mic:
    index1 = devices[devices.find(mic):]
    index2 = index1.find('"')
    MICROFONE = index1[:index2]
    print(MICROFONE)
else:
    print(devices)

# MICROFONE = "\u041c\u0438\u043a\u0440\u043e\u0444\u043e\u043d (Realtek High Definition Audio)"
# MICROFONE = "@device_cm_{33D9A762-90C8-11D0-BD43-00A0C911CE86}\wave_{B78A07E2-554B-41DF-8F73-A7EA6662A7A0}"
# import json
# MICROFONE = json.loads(json.dumps("Микрофон (Realtek High Definition Audio)", ensure_ascii=False))
