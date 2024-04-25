
import pyautogui
import time

def type_with_delay(text, delay=0.01):
    for char in text:
        pyautogui.write(char)
        time.sleep(delay)

def clean_and_convert_to_int(input_string):
    # Entfernen aller Zeichen, die keine Ziffern sind
    cleaned_string = ''.join(c for c in input_string if c.isdigit())
    # Konvertieren in eine Ganzzahl
    return int(cleaned_string)