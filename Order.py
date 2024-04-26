class Order:
    def __init__(self, item_name, max_buy_price, min_sell_price, quantity):
        self.item_name = item_name
        self.max_buy_price = max_buy_price
        self.min_sell_price = min_sell_price
        self.quantity = quantity

    def __str__(self):
        return (f"Order - Item: {self.item_name}, Max Buy Price: {self.max_buy_price}, "
                f"Min Sell Price: {self.min_sell_price}, Quantity: {self.quantity}")
