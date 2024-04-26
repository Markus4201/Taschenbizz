from ActionFunctions import *
from watchdog import *


def main():
    setup_watchdog()
    # Hauptfunktionalität
    create_sell_order(item_name="Tasche des Adepten", quantity=1, minimum_difference=5)
    collect_items()
    #update_buy_order(item_name="Tasche des Adepten", quantity=1, minimum_difference=5,max_pay_amount=2000)

if __name__ == "__main__":
    main()

