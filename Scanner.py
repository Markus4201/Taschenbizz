import numpy as np
from PIL import ImageGrab
import matplotlib.pyplot as plt
import pytesseract
import cv2
import pyautogui


def clean_string(input_string):
    # Ersetzt Zeilenumbrüche durch Leerzeichen
    cleaned_string = ' '.join(input_string.splitlines())

    # Entfernt führende und abschließende Leerzeichen und korrigiert mehrfache Leerzeichen innerhalb des Strings
    cleaned_string = ' '.join(cleaned_string.split())

    return cleaned_string


def scan_string_in_region(region, showImage=False):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    pyautogui.moveTo(region[0],region[1])
    # Bildschirmaufnahme des spezifizierten Bereichs
    screen = np.array(ImageGrab.grab(bbox=region))

    # Bild anzeigen, wenn showImage True ist
    if showImage:
        plt.imshow(screen, cmap='gray')
        plt.title("Verarbeitetes Bild für OCR")
        plt.show()

    # OCR-Konfiguration für Textextraktion
    custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist= abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZäöüÄÖÜß'
    extracted_text = pytesseract.image_to_string(screen, config=custom_config)
    print("Scanned String: ", extracted_text)

    return clean_string(extracted_text)


def clean_and_convert_to_int(input_string):
    # Entfernen aller Zeichen, die keine Ziffern sind
    cleaned_string = ''.join(c for c in input_string if c.isdigit())
    # Konvertieren in eine Ganzzahl
    return int(cleaned_string) if cleaned_string else 0


def scan_number_in_region(region, showImage=False):
    pyautogui.moveTo(region[0],region[1])
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    # Bildschirmaufnahme des spezifizierten Bereichs
    screen = np.array(ImageGrab.grab(bbox=region))

    # Bild anzeigen, wenn showImage True ist
    if showImage:
        plt.imshow(screen, cmap='gray')
        plt.title("Verarbeitetes Bild für OCR")
        plt.show()

    # OCR-Konfiguration für Zahlenextraktion
    custom_config = r'--oem 3 --psm 6 outputbase digits'
    extracted_text = pytesseract.image_to_string(screen, config=custom_config)

    print("Scanned Number: ",str(clean_and_convert_to_int(extracted_text)))

    # Rückgabe der bereinigten und konvertierten Zahl
    return clean_and_convert_to_int(extracted_text)


def is_similar(screen_region, template_path, threshold=0.8, showImage=False):
    # Lade das Template-Bild
    template = cv2.imread(template_path, 0)  # 0 bedeutet, dass es in Graustufen geladen wird
    screen = np.array(ImageGrab.grab(bbox=screen_region))
    screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

    if showImage:
        plt.imshow(screen, cmap='gray')
        plt.title("Verarbeitetes Bild für OCR")
        plt.show()

    # Template Matching durchführen
    result = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, _ = cv2.minMaxLoc(result)

    # Prüfe, ob die Ähnlichkeit über dem Schwellenwert liegt
    return max_val >= threshold