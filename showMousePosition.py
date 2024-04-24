import pyautogui
import time

try:
    while True:
        x, y = pyautogui.position()  # Aktuelle Position der Maus als Tupel (x, y)
        print(f"Mausposition: x={x}, y={y}\n", end='\r')
        time.sleep(1)  # kurze Pause, um die Ausgabe lesbar zu machen
except KeyboardInterrupt:
    print("\nProgramm durch Benutzer abgebrochen.")
