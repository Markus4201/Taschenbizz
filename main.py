from ActionFunctions import *
from Order import Order
from watchdog import *

orders = [
Order("Pirschjägerschuhe des Adepten", 700, 1000, 5),
    Order("Maultier des Novizen", 1800, 1800, 5),
    Order("Transportochse des Gesellen", 7000, 10000, 5),
    Order("Tasche des Adepten", 2000, 2000, 5),

    Order("Klerikergugel des Adepten", 400, 600, 5),
    Order("Pirschjägerschuhe des Adepten", 700, 1000, 5),
    Order("Pirschjägerjacke des Adepten", 3500, 5500, 2),
    Order("Kürschner-Arbeitsschuhe des Adepten", 600, 1000, 5),
    Order("Naturstab des Adepten", 1800, 2400, 5),
    Order("Druidenstab des Adepten", 1200, 2600, 5),
    Order("Blutklinge des Adepten", 4000, 8000, 3),


]
DIFF = 5


def main():
    setup_watchdog()

    while True:
        for order in orders:
            status = update_buy_order(order.item_name, order.quantity, DIFF, order.max_buy_price)
            if status == "NO_BUY_ORDER":
                create_buy_order(order.item_name, order.quantity, DIFF)
            #update_sell_order(order.item_name, order.quantity, DIFF, order.min_sell_price)
            collect_items()
            create_sell_order(order.item_name, order.quantity, DIFF)


if __name__ == "__main__":
    main()
