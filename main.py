import pytesseract
import numpy as np
from PIL import ImageGrab
import matplotlib.pyplot as plt
from Utility.window_detect import getAlbionPos
from ActionFunctions import *
import pyautogui
import time







# Position des Spielfensters ermitteln
X, Y = getAlbionPos()
print("Albion is at", X, Y)

pyautogui.click(340, 180)
time.sleep(0.1)

# Beispielregionen
region_of_interest = (X, Y, X+100, Y+100)  # Beliebiger Bereich
first_sell_order = (X+700, Y+272, X+700+37, Y+272+14)  # Spezifischer Bereich für ersten Verkaufsauftrag

# Text und Zahlen extrahieren
#print(ScanNumberInRegion((X+700, Y+272, X+737, Y+288), True))
print(create_buy_order(item_name="Tasche des Adepten",quantity=10,minimum_difference=1))


