import threading
import signal
import keyboard

def handle_quit_signal(signum, frame):
    print("Beenden des Programms durch Signal...")
    raise SystemExit

def keypress_watchdog():
    print("Drücken Sie 'Q' um das Programm zuq beenden...")
    keyboard.wait('ESC')
    signal.raise_signal(signal.SIGINT)
def setup_watchdog():
    signal.signal(signal.SIGINT, handle_quit_signal)
    watchdog_thread = threading.Thread(target=keypress_watchdog)
    watchdog_thread.daemon = True
    watchdog_thread.start()