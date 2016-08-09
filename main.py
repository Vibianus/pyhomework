import pyHook
import pythoncom
from time import *

position = 1

def onKeyboardEvent(event):
    global position
    if event.Key == "Up":
        if position > 3 :
            position = position - 3
            print('往上 位置在', position )
            
    if event.Key == "Down":
        if position < 7 :
            position = position + 3
            print('往下 位置在', position )
            
    if event.Key == "Left":
        if not position in [1, 4, 7] :
            position = position - 1
            print('往左 位置在', position )
    
    if event.Key == "Right":
        if not position in [3, 6, 9] :
            position = position + 1
            print('往右 位置在', position )

    return True
    

    

def main():
    hm = pyHook.HookManager()
    hm.KeyDown = onKeyboardEvent
    hm.HookKeyboard()
    pythoncom.PumpMessages()

if __name__ == "__main__":
    main()
