import sys
import time

import pyautogui

from Scanner import scan_number_in_region, scan_string_in_region


def type_with_delay(text, delay=0.01):
    for char in text:
        pyautogui.write(char)
        time.sleep(delay)


def clean_and_convert_to_int(input_string):
    # Entfernen aller Zeichen, die keine Ziffern sind
    cleaned_string = ''.join(c for c in input_string if c.isdigit())
    # Konvertieren in eine Ganzzahl
    return int(cleaned_string)


def click(position):
    pyautogui.moveTo(position, duration=2)
    pyautogui.click()


def check_open_orderoverview(positions):
    # Hier wird überprüft, ob die Order-Übersicht bereits geöffnet ist
    order_overview = scan_number_in_region(positions.ORDER_OVERVIEW_REGION)
    print("Order overview check:", order_overview)
    if not order_overview:
        click(positions.ORDER_OVERVIEW_TOGGLE_POS)
        order_overview = scan_number_in_region(positions.ORDER_OVERVIEW_REGION)
        if not order_overview:
            print("Fehler: Preisübersicht konnte nicht geöffnet werden.")
            sys.exit()


def scan_top_orders(positions, minimum_difference):
    # Scanne beste Buy und Sell Order
    sell_price = scan_number_in_region(positions.ORDER_OVERVIEW_REGION)
    buy_price = scan_number_in_region(positions.BEST_BUY_PRICE_REGION)

    print("Detected Prices:", buy_price, sell_price)
    if not sell_price or not buy_price or (sell_price - buy_price) * 100 / sell_price <= minimum_difference:
        print("Fehler: Preisunterschied nicht groß genug.")
        sys.exit()


def check_existing_order(item_name, positions):
    scanned_name = scan_string_in_region(positions.MY_ORDER_ITEM_NAME)  # Annahme: die Region ist hier korrekt
    print("Scanned name:", scanned_name)
    if scanned_name.strip().lower() != item_name.lower():
        print("Fehler: Order für das Item nicht gefunden.")
        sys.exit()

    item_count = scan_number_in_region(positions.CURRENT_ORDER_AMOUNT_REGION, True)

    # Aktuellen Order Preis merken
    item_price = scan_number_in_region(positions.CURRENT_ORDER_PRICE_REGION,True)
    print("Order has", item_count, "items, and price is:", item_price)
    return item_count, item_price
