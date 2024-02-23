import pyperclip
import re
import time
import keyboard as kb
from pynput.keyboard import Controller
import uuid

keyboard_controller = Controller()

def get_mac_address():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ':'.join([mac[e:e+2] for e in range(0, 11, 2)])

def write():
    mac_address = get_mac_address()
    if mac_address == "sample":
        time.sleep(3)
        copied_text = pyperclip.paste()
        # copied_text = re.sub(r'[\n\t]', '', copied_text)
        copied_text = re.sub(r'^[ \t]+', '', copied_text, flags=re.MULTILINE)
        copied_text = re.sub(r'\n', '', copied_text)
        keyboard_controller.type(copied_text)
    else:
        time.sleep(3)
        copied_text = "You are not Authorized to use AutoTyper"
        # copied_text = re.sub(r'[\n\t]', '', copied_text)
        copied_text = re.sub(r'^[ \t]+', '', copied_text, flags=re.MULTILINE)
        copied_text = re.sub(r'\n', '', copied_text)
        keyboard_controller.type(copied_text)

kb.add_hotkey('alt + ctrl + v', write)
kb.wait('esc')
