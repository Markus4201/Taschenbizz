from ActionFunctions import *
from Order import Order
from watchdog import *

orders = [
    Order("Söldnerjacke des Adepten", 1000, 1000, 5),
    Order("Tasche des Adepten", 2000, 2000, 5),
    Order("Maultier des Novizen", 1800, 1800, 5),
    Order("Klerikergugel des Adepten", 400, 600, 5),

]
DIFF = 5


def main():
    setup_watchdog()

    while True:
        for order in orders:
            status = update_buy_order(order.item_name, order.quantity, DIFF, order.max_buy_price)
            if status == "NO_BUY_ORDER":
                create_buy_order(order.item_name, order.quantity, DIFF)
            update_sell_order(order.item_name, order.quantity, DIFF, order.min_sell_price)
            collect_items()
            create_sell_order(order.item_name, order.quantity, DIFF)

    # create_sell_order(item_name="Tasche des Adepten", quantity=1, minimum_difference=5)
    # collect_items()
    # update_sell_order(item_name="Tasche des Adepten", quantity=3, minimum_difference=5, min_sell_amount=1300)


if __name__ == "__main__":
    main()
