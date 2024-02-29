import pyperclip
import re
import time
import keyboard as kb
from pynput.keyboard import Controller

keyboard_controller = Controller()

def write():
        time.sleep(3)
        copied_text = pyperclip.paste()
        # copied_text = re.sub(r'[\n\t]', '', copied_text)
        copied_text = re.sub(r'^[ \t]+', '', copied_text, flags=re.MULTILINE)
        copied_text = re.sub(r'\n', '', copied_text)
        keyboard_controller.type(copied_text)
    
kb.add_hotkey('alt + ctrl + v', write)
kb.wait('ctrl + win + esc')

