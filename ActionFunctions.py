import numpy as np
from PIL import ImageGrab
import matplotlib.pyplot as plt
import pytesseract
import pyautogui
import time
from Utility.window_detect import getAlbionPos


def clean_and_convert_to_int(input_string):
    # Entfernen aller Zeichen, die keine Ziffern sind
    cleaned_string = ''.join(c for c in input_string if c.isdigit())
    # Konvertieren in eine Ganzzahl
    return int(cleaned_string)


def create_buy_order(item_name, quantity, minimum_difference):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    X, Y = getAlbionPos()
    # Klick auf Eingabefeld
    pyautogui.click(X + 340, Y + 180)
    time.sleep(0.1)

    # Eingabe des Itemnamens
    pyautogui.write(item_name)
    time.sleep(1)

    # "Kaufen" Button anklicken
    pyautogui.click(X + 930, Y + 330)
    time.sleep(0.1)

    # Überprüfen, ob Orderübersicht aufgeklappt ist
    order_overview = ScanNumberInRegion((X + 700, Y + 272, X + 737, Y + 288))
    if not order_overview:  # Falls der Bereich leer ist, klicken, um zu öffnen
        pyautogui.click(X + 1055, Y + 148)
        time.sleep(0.1)
        order_overview = ScanNumberInRegion((X + 700, Y + 272, X + 737, Y + 288))
        if not order_overview:
            return "Fehler: Preisübersicht konnte nicht geöffnet werden."

    # Scanne beste Buy und Sell Order
    sell_price_string = ScanNumberInRegion((X + 700, Y + 272, X + 737, Y + 288))
    sell_price = clean_and_convert_to_int(sell_price_string)
    buy_price_string = ScanNumberInRegion((X + 925, Y + 272, X + 962, Y + 288))
    buy_price = clean_and_convert_to_int(buy_price_string)

    print("Detected Prices:", buy_price, sell_price)

    # Überprüfe Differenz der Preise
    print((sell_price - buy_price) / float(sell_price))
    if not sell_price or not buy_price or (sell_price - buy_price)*100 / sell_price <= minimum_difference:
        return "Fehler: Preisunterschied nicht groß genug."

    # Prozess zur Erstellung der Kauforder
    pyautogui.click(X + 276, Y + 430)  # Klick auf "Kauforder"
    time.sleep(0.1)
    for _ in range(quantity-1):  # Klicke (+) bei Anzahl
        pyautogui.click(X + 557, Y + 484)
        time.sleep(0.1)
    pyautogui.click(X + 554, Y + 518)  # Klicke auf (+) bei Preis
    time.sleep(0.1)
    pyautogui.click(X + 571, Y + 608)  # Klicke auf "Kauforder erstellen"
    time.sleep(0.1)
    # pyautogui.click(X+527, Y+450)  # Klicke auf "Ja"
    # time.sleep(0.1)
    #
    # return "Kauforder erfolgreich erstellt."


# Methode, um Zahlen in einem bestimmten Bereich zu scannen
def ScanNumberInRegion(region, showImage=False):
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

    print("extracted text: " + extracted_text)

    return extracted_text
