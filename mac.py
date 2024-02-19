import pyperclip
import keyboard as kb
from pynput.keyboard import Controller

import time
import re


keyboard_controller = Controller()

def singleline2():
    time.sleep(3)
    copied_text = pyperclip.paste()
    # copied_text = re.sub(r'[\n\t]', '', copied_text)
    copied_text = re.sub(r'^[ \t]+', '', copied_text, flags=re.MULTILINE)
    copied_text = re.sub(r'\n','',copied_text)

    keyboard_controller.type(copied_text)

def transform_text_to_single_line(text):
  result = " ".join(line.strip() for line in text.splitlines())

  return result

def text():
    time.sleep(3)
    multiline_text = pyperclip.paste()
    # single_line_text = transform_text_to_single_line(multiline_text)
    keyboard_controller.type(multiline_text)
    # pyperclip.copy(single_line_text)

        
# kb.add_hotkey('ctrl+7', singleline2)
kb.add_hotkey('alt + v', singleline2)
# kb.add_hotkey('ctrl+8',text)
kb.wait('esc') 
# kb.remove_hotkey('alt+ctrl+v')

