from ActionFunctions import *
from watchdog import *

items = ["Tasche des Adepten", "Maultier"]
def main():
    setup_watchdog()

    #while True:
    #    for item in items:
    #        update_buy_order()
    # Hauptfunktionalität
    #create_sell_order(item_name="Tasche des Adepten", quantity=1, minimum_difference=5)
    #collect_items()
    update_sell_order(item_name="Tasche des Adepten", quantity=3, minimum_difference=5,min_sell_amount=1300)

if __name__ == "__main__":
    main()

