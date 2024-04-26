from ActionFunctions import *
from watchdog import *


def main():
    setup_watchdog()
    # Hauptfunktionalität
    create_buy_order(item_name="Tasche des Adepten", quantity=1, minimum_difference=5)

if __name__ == "__main__":
    main()

