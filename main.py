from pyautogui import dragTo,position 
from keyboard import is_pressed 
 
# https://www.geeksforgeeks.org/mouse-keyboard-automation-using-python/
print('THE PROGRAM IS RUNNING')
while True: 
    try:  
        if is_pressed('r'):
        	x,y=tuple(position())
        	dragTo(x+20,y+20, duration = 1/50)
        	dragTo(x+20+150,y+20-150, duration = 1/50)
        elif is_pressed('w'):
        	x,y=tuple(position())
        	dragTo(x+50,y+50, duration = 1/200)
        	dragTo(x+25,y+25, duration = 1/200)
        	dragTo(x+25+25,y+25-25, duration = 1/200)
        	dragTo(x+25-25,y+25+25, duration = 1/200)
        elif is_pressed('q'):
        	break
        else:
        	pass
    except:
        break 
print('THE PROGRAM HAS ENDED')