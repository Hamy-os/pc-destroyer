import subprocess
import os
import requests
import time
import datetime
import keyboard
import asyncio

def check_time():
    date = datetime.datetime.now()
    year = date.year
    month = date.month
    day = date.day
    hour = date.hour
    minute = date.minute
    second = date.second
    if year == 2022 and month == 9 and day == 20 and hour == 8 and minute == 0 and second == 00:
        return False
    elif year == 2022 and month == 9 and day == 22 and hour == 10 and minute == 20 and second == 00:
        return False
    else:
        return True

def destroy_pc():
    print("Destroying PC...")
    #time.sleep(1)
    video_URL = "https://cdn.discordapp.com/attachments/1019979931947630682/1019979958329819196/Saul_goodman_3d.mp4"
    r = requests.get(video_URL, allow_redirects=True)
    with open('video.mp4', 'wb') as fd:
        fd.write(r.content)
    # run the volume.vbs file then print hello
    
    subprocess.Popen(['cscript', 'volume.vbs'])
    subprocess.Popen(['cscript', 'video.vbs'])
    time.sleep(15)
    print("Hello")


destroy_pc()

"""
while True:
    if check_time():
        print("It is not time yet")
        time.sleep(1)
    else:
        print("It is time")
        destroy_pc()
    time.sleep(1)
"""