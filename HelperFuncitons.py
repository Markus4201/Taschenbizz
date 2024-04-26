import sys
import time

import pyautogui
from Levenshtein import distance as levenshtein_distance
from Scanner import scan_number_in_region, scan_string_in_region


def type_with_delay(text, delay=0.003):
    for char in text:
        pyautogui.write(char)
        time.sleep(delay)




def click(position):
    pyautogui.moveTo(position, duration=1)
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


def scan_top_orders(positions, minimum_difference):
    # Scanne beste Buy und Sell Order
    sell_price = scan_number_in_region(positions.ORDER_OVERVIEW_REGION)
    buy_price = scan_number_in_region(positions.BEST_BUY_PRICE_REGION)

    print("Detected Prices:", buy_price, sell_price)
    if not sell_price or not buy_price or (sell_price - buy_price) * 100 / sell_price <= minimum_difference:
        print("Fehler: Preisunterschied nicht groß genug.")
        click(positions.CLOSE_BUTTON)
        return -1,-1
    return sell_price, buy_price


def check_existing_buy_order(item_name, positions):
    scanned_name = scan_string_in_region(positions.MY_BUY_ORDER_ITEM_NAME)  # Annahme: die Region ist hier korrekt
    print("Scanned name:", scanned_name)
    if not are_strings_similar(item_name,scanned_name):
        print("Fehler: Order für das Item nicht gefunden.")
        return -1,-1

    item_count = scan_number_in_region(positions.CURRENT_BUY_ORDER_AMOUNT_REGION, )

    # Aktuellen Order Preis merken
    item_price = scan_number_in_region(positions.CURRENT_BUY_ORDER_PRICE_REGION, )
    print("Order has", item_count, "items, and price is:", item_price)
    return item_count, item_price

def check_existing_sell_order(item_name, positions):
    scanned_name = scan_string_in_region(positions.MY_SELL_ORDER_ITEM_NAME)  # Annahme: die Region ist hier korrekt
    print("Scanned name:", scanned_name)
    if not are_strings_similar(item_name,scanned_name):
        print("Fehler: Order für das Item nicht gefunden.")
        return -1,-1

    item_count = scan_number_in_region(positions.CURRENT_SELL_ORDER_AMOUNT_REGION, )

    # Aktuellen Order Preis merken
    item_price = scan_number_in_region(positions.CURRENT_SELL_ORDER_PRICE_REGION, )
    print("Order has", item_count, "items, and price is:", item_price)
    return item_count, item_price

def updateQuantity(current_quantity, target_quantity, positions):
    print("found", current_quantity, "items, setting it to:", target_quantity)
    if target_quantity > current_quantity:
        # Die gewünschte Quantität ist größer als die aktuelle, erhöhe die Quantität
        increment_amount = target_quantity - current_quantity
        for _ in range(increment_amount):
            click(positions.INCREASE_QUANTITY_POS)
            time.sleep(0.1)  # Kurze Pause, um sicherzustellen, dass das UI reagieren kann
        print(f"Quantität wurde um {increment_amount} erhöht.")

    elif target_quantity < current_quantity:
        # Die gewünschte Quantität ist kleiner als die aktuelle, verringere die Quantität
        decrement_amount = current_quantity - target_quantity
        for _ in range(decrement_amount):
            click(positions.DECREASE_QUANTITY_POS)
            time.sleep(0.1)  # Kurze Pause, um sicherzustellen, dass das UI reagieren kann
        print(f"Quantität wurde um {decrement_amount} verringert.")
    else:
        # Die gewünschte Quantität ist gleich der aktuellen Quantität
        print("Keine Anpassung der Quantität erforderlich.")


def are_strings_similar(str1, str2, max_distance=5):
    """
    Überprüft, ob zwei Strings ähnlich sind, basierend auf der Levenshtein-Distanz.

    Args:
    str1 (str): Erster String.
    str2 (str): Zweiter String.
    max_distance (int): Maximale Anzahl an Änderungen, die für eine Ähnlichkeit akzeptabel sind.

    Returns:
    bool: True, wenn die Strings als ähnlich betrachtet werden, sonst False.
    """
    # Berechnen der Levenshtein-Distanz zwischen den beiden Strings
    dist = levenshtein_distance(str1, str2)

    # Vergleichen der Distanz mit dem maximal erlaubten Schwellenwert
    return dist <= max_distance