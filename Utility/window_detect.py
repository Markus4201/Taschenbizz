import win32gui
import time

pos = [2]*2
size = [2]
floX = -1
floY = -1
floW = -1
floH = -1

    
def callback(hwnd, extra):
    rect = win32gui.GetWindowRect(hwnd)
    x = rect[0]
    y = rect[1]
    w = rect[2] - x
    h = rect[3] - y
    #print("Window %s:" % win32gui.GetWindowText(hwnd)[:9])
    #print("\tLocation: (%d, %d)" % (x, y))
    #print("\t    Size: (%d, %d)" % (w, h))
    if(win32gui.GetWindowText(hwnd)[:6] == 'Albion'):
        pos[0] = rect[0]
        pos[1] = rect[1]
        floW = rect[2] - x
        floH = rect[3] - y
        
        
def getAlbionPos():
    win32gui.EnumWindows(callback, None)
    return pos[0], pos[1]

def getAlbionSize():
    win32gui.EnumWindows(callback, None)
    return floW, floH

x,y = getAlbionPos()
print(x,y)
