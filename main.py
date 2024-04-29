import time

from ActionFunctions import *
from NicePriceFinder import findNicePrice
from Order import Order
from watchdog import *

orders = [
Order("Pirschjägerschuhe des Adepten", 800, 1500, 2),
    Order("Maultier des Novizen", 2000, 2500, 5),
    Order("Transportochse des Gesellen", 7000, 8000, 1),
    Order("Tasche des Adepten", 2000, 2000, 5),

    #Order("Klerikergugel des Adepten", 400, 600, 5),
    #Order("Pirschjägerschuhe des Adepten", 700, 1000, 5),
    Order("Pirschjägerjacke des Adepten", 4500, 7000, 2),
    Order("Kürschner-Arbeitsschuhe des Adepten", 600, 1000, 5),
    #Order("Naturstab des Adepten", 1800, 2400, 5),
    Order("Druidenstab des Adepten", 1200, 2600, 5),
    #Order("Blutklinge des Adepten", 4000, 8000, 3),
    Order("Reitpferd des Gesellen", 8200, 9000, 1),


]
DIFF = 5


def main():
    setup_watchdog()

    findNicePrice()

    # while True:
    #     for order in orders:
    #         status = update_buy_order(order.item_name, order.quantity, DIFF, order.max_buy_price)
    #         if status == "NO_BUY_ORDER":
    #             create_buy_order(order.item_name, order.quantity, DIFF)
    #         #update_sell_order(order.item_name, order.quantity, DIFF, order.min_sell_price)
    #         collect_items()
    #         create_sell_order(order.item_name, order.quantity, DIFF)
    #         #time.sleep(100)


if __name__ == "__main__":
    main()
