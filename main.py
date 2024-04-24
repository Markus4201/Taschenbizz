from ActionFunctions import *
import pyautogui
import time

# Position des Spielfensters ermitteln
X, Y = getAlbionPos()
print("Albion is at", X, Y)
time.sleep(0.1)

update_buy_order(item_name="Tasche des Adepten",quantity=10,minimum_difference=1,max_pay_amount=2000)
update_buy_order(item_name="Tasche des Adepten",quantity=10,minimum_difference=5,max_pay_amount=2000)
#create_buy_order(item_name="Tasche des Adepten",quantity=10,minimum_difference=1)
#collect_items()


