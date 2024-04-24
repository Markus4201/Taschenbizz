import numpy as np
from PIL import ImageGrab
import matplotlib.pyplot as plt
import pytesseract


def scan_string_in_region(region, showImage=False):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    # Bildschirmaufnahme des spezifizierten Bereichs
    screen = np.array(ImageGrab.grab(bbox=region))

    # Bild anzeigen, wenn showImage True ist
    if showImage:
        plt.imshow(screen, cmap='gray')
        plt.title("Verarbeitetes Bild für OCR")
        plt.show()

    # OCR-Konfiguration für Textextraktion
    extracted_text = pytesseract.image_to_string(screen)
    print("Scanned String: ", extracted_text)

    return extracted_text


def clean_and_convert_to_int(input_string):
    # Entfernen aller Zeichen, die keine Ziffern sind
    cleaned_string = ''.join(c for c in input_string if c.isdigit())
    # Konvertieren in eine Ganzzahl
    return int(cleaned_string) if cleaned_string else 0


def scan_number_in_region(region, showImage=False):
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
