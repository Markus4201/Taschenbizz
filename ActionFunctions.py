import pyautogui
import time
from Utility.window_detect import getAlbionPos
from Scanner import scan_number_in_region, scan_string_in_region, is_similar
from HelperFuncitons import type_with_delay
from PositionVariables import *


def create_buy_order(item_name, quantity, minimum_difference):
    positions = PositionConfig()
    pyautogui.click(positions.ITEM_NAME_ENTRY_POS)
    time.sleep(0.1)
    pyautogui.write(item_name)
    time.sleep(1)
    pyautogui.click(positions.BUY_BUTTON_POS)
    time.sleep(0.1)

    # Hier wird überprüft, ob die Order-Übersicht bereits geöffnet ist
    order_overview = scan_number_in_region(positions.ORDER_OVERVIEW_REGION)
    print(order_overview)
    if not order_overview:
        pyautogui.moveTo(positions.ORDER_OVERVIEW_TOGGLE_POS)
        time.sleep(6)
        pyautogui.click()
        time.sleep(0.1)
        order_overview = scan_number_in_region(positions.ORDER_OVERVIEW_REGION)
        if not order_overview:
            print("Fehler: Preisübersicht konnte nicht geöffnet werden.")
            return

    # Scanne beste Buy und Sell Order
    sell_price = scan_number_in_region(positions.ORDER_OVERVIEW_REGION)
    buy_price = scan_number_in_region(positions.BEST_BUY_PRICE_REGION)

    print("Detected Prices:", buy_price, sell_price)
    if not sell_price or not buy_price or (sell_price - buy_price) * 100 / sell_price <= minimum_difference:
        print("Fehler: Preisunterschied nicht groß genug.")
        return

    pyautogui.click(positions.BUY_ORDER_POS)
    time.sleep(0.1)
    for _ in range(quantity - 1):
        pyautogui.click(positions.INCREASE_QUANTITY_POS)
        time.sleep(0.1)
    pyautogui.click(positions.INCREASE_PRICE_POS)
    time.sleep(0.1)
    pyautogui.click(positions.CONFIRM_ORDER_POS)
    time.sleep(0.1)
    pyautogui.click(positions.CONFIRM_YES_POS)
    time.sleep(0.1)

    print("Kauforder erfolgreich erstellt.")
    return


def update_buy_order(item_name, quantity, minimum_difference, max_pay_amount):
    X, Y = getAlbionPos()

    # Klick auf "Meine Orders"
    pyautogui.moveTo(X + 1033, Y + 470, duration=0.3)
    pyautogui.click()

    # Klick auf Eingabefeld
    pyautogui.moveTo(X + 340, Y + 180, duration=0.3)
    pyautogui.click()
    type_with_delay(item_name)

    # Überprüfe ob Order vorhanden
    scanned_name = scan_string_in_region((X + 391, Y + 302, X + 531, Y + 321))
    print("Scanned name:", scanned_name)
    if scanned_name.strip().lower() != item_name.lower():
        print("Fehler: Order für das Item nicht gefunden.")
        return

    # Anzahl der Items merken
    item_count = scan_number_in_region((X + 540, Y + 300, X + 584, Y + 320))

    # Aktuellen Order Preis merken
    item_price = scan_number_in_region((X + 734, Y + 300, X + 834, Y + 322))

    # Klicke auf Bearbeiten
    pyautogui.moveTo(X + 892, Y + 311, duration=0.3)
    pyautogui.click()
    time.sleep(0.2)

    # Überprüfen, ob Preisübersicht geöffnet ist (ähnlich wie in create_buy_order)
    order_overview = scan_number_in_region((X + 700, Y + 272, X + 737, Y + 288))
    if not order_overview:  # Falls der Bereich leer ist, klicken, um zu öffnen
        pyautogui.moveTo(X + 916, Y + 233, duration=0.3)
        pyautogui.click()
        order_overview = scan_number_in_region((X + 700, Y + 272, X + 737, Y + 288))
        if not order_overview:
            print("Fehler: Preisübersicht konnte nicht geöffnet werden.")
            return

    # Scanne beste Buy Order
    best_buy_price = scan_number_in_region((X + 925, Y + 272, X + 962, Y + 288))

    # Setze Preis auf gescannten Preis +1, falls < maxPayAmount
    new_price = best_buy_price + 1
    if item_price == best_buy_price:
        print("Deine Order ist noch die Beste")
    else:
        if new_price < max_pay_amount:
            pyautogui.moveTo(X + 350, Y + 517, duration=0.3)  # Klicke auf Eingabefeld für Preis
            pyautogui.click()
            pyautogui.write(str(new_price))  # Eingabe des neuen Preises
        else:
            print("Fehler: Maximaler Zahlbetrag überschritten.")
            return

    # Klicke (+) bei Anzahl bis gewünschte Anzahl wieder erreicht
    for _ in range(quantity - item_count):
        pyautogui.moveTo(X + 557, Y + 484, duration=0.6)
        pyautogui.click()

    # Klicke auf Order Aktualisieren
    pyautogui.moveTo(X + 571, Y + 608, duration=1)
    pyautogui.click()

    print("Kauforder erfolgreich aktualisiert.")
    return


def collect_items():
    X, Y = getAlbionPos()
    # region in der das "check" symbol sichtbar sein sollte
    screen_region = (X + 1022, Y + 616, X + 1043, Y + 636)
    template_path = 'assets/check.png'
    if is_similar(screen_region, template_path):
        # Bewegen zum Button "Abgeschlossene Handel" und klicken
        pyautogui.moveTo(X + 1040, Y + 615, duration=0.3)
        pyautogui.click()

        time.sleep(0.5)

        # Bewegen zum Button "Alles einsammeln" und klicken
        pyautogui.moveTo(X + 940, Y + 750, duration=0.3)
        pyautogui.click()

        print("Items erfolgreich eingesammelt.")
    else:
        print("Keine Abholbereiten items erkannt")
