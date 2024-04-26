import pyautogui
import time

import sys
from Utility.window_detect import getAlbionPos
from Scanner import scan_number_in_region, scan_string_in_region, is_similar
from HelperFuncitons import *
from PositionVariables import *


def create_buy_order(item_name, quantity, minimum_difference):
    positions = PositionConfig()

    click(positions.ITEM_NAME_ENTRY_POS)
    type_with_delay(item_name)
    click(positions.BUY_BUTTON_POS)
    check_open_orderoverview(positions)
    scan_top_orders(positions, minimum_difference)
    click(positions.BUY_ORDER_POS)

    for _ in range(quantity - 1):
        click(positions.INCREASE_QUANTITY_POS)

    click(positions.INCREASE_PRICE_POS)
    click(positions.CONFIRM_ORDER_POS)
    click(positions.CONFIRM_YES_POS)

    print("Kauforder erfolgreich erstellt.")
    return


def update_buy_order(item_name, quantity, minimum_difference, max_pay_amount):
    positions = PositionConfig()

    click(positions.MY_ORDERS_POS)
    click(positions.ITEM_NAME_ENTRY_POS)
    type_with_delay(item_name)

    item_count, item_price = check_existing_order(item_name,positions)

    click(positions.EDIT_BUTTON_POS)

    check_open_orderoverview(positions)

    # Scanne beste Buy Order
    best_buy_price = scan_number_in_region(positions.BEST_BUY_PRICE_REGION)

    # Setze Preis auf gescannten Preis +1, falls < maxPayAmount
    new_price = best_buy_price + 1
    if item_price == best_buy_price:
        print("Deine Order ist noch die Beste")
    else:
        if new_price < max_pay_amount:
            click(positions.INCREASE_PRICE_POS)
            type_with_delay(str(new_price))
        else:
            print("Fehler: Maximaler Zahlbetrag überschritten.")
            sys.exit()

    # Klicke (+) bei Anzahl bis gewünschte Anzahl wieder erreicht
    for _ in range(quantity - item_count):
        click(positions.INCREASE_QUANTITY_POS)

    click(positions.CONFIRM_ORDER_POS)

    print("Kauforder erfolgreich aktualisiert.")


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
