import pyHook
import pythoncom
import drawboard
import monster
import random
import os
from time import *

position = 1
game_over = False
exit = random.randint(2,9) 

def onKeyboardEvent(event):
    global game_over
    if game_over:
        return True

    global position
    global exit
    cur_position = position
    if event.Key == "Up":
        if position > 3 :
            position = position - 3
            print('往上 位置在', position )
            
    elif event.Key == "Down":
        if position < 7 :
            position = position + 3
            print('往下 位置在', position )
            
    elif event.Key == "Left":
        if not position in [1, 4, 7] :
            position = position - 1
            print('往左 位置在', position )
    
    elif event.Key == "Right":
        if not position in [3, 6, 9] :
            position = position + 1
            print('往右 位置在', position )
    
    if position == exit :
        drawboard.drawboard( position )
        print('Exit Success! You win!')
        game_over = True 
        os._exit(1)
        
    if cur_position != position :
        drawboard.drawboard( position )
        if monster.moster_position(position) :
            print('Monster got you. Game Over!')
            game_over = True 
            os._exit(1)

    return True
    

    

def main():
    global position
    drawboard.drawboard( position )
    print('X=你的位置')
    print('上下左右移動')
    hm = pyHook.HookManager()
    hm.KeyDown = onKeyboardEvent
    hm.HookKeyboard()
    pythoncom.PumpMessages()

if __name__ == "__main__":
    main()
