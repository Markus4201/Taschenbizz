import time

class MainController:
    def __init__(self):
        self.ui_automation = UIAutomation()
        self.order_management = OrderManagement()
        self.item_management = ItemManagement()
        self.price_scanner = PriceScanner()
        self.running = True

    def run(self):
        while self.running:
            try:
                # Überprüfe, ob gekaufte Items abgeholt werden können
                self.item_management.check_for_bought_items()
                self.item_management.collect_bought_items()

                # Überprüfe und aktualisiere Buy/Sell Orders
                self.order_management.check_current_buy_orders()
                self.order_management.update_buy_order()
                self.order_management.check_current_sell_orders()
                self.order_management.update_sell_order()

                # Erstelle neue Orders basierend auf Marktbedingungen
                price_info = self.price_scanner.scan_buy_sell_orders()
                if price_info["price_difference"] >= MINIMUM_DIFFERENCE:
                    self.order_management.create_buy_order("Item Name", 10, MINIMUM_DIFFERENCE)

                # Pause zwischen den Iterationen
                time.sleep(10)  # Pause für 10 Sekunden
            except Exception as e:
                print(f"An error occurred: {e}")
                self.running = False

# Beispiel-Nutzung
if __name__ == "__main__":
    controller = MainController()
    controller.run()
