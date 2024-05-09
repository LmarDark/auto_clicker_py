import mouse
import keyboard as kb
from time import sleep as s

while True:
    try:
        totalTime = float(input("Click's per second:"))
        totalTime_Verify = isinstance(totalTime, (float, int))
        if(totalTime_Verify == True):
            break
    except:
        print("Please enter a valid number")

while True:
    try:
        s(totalTime)
        mouse.click() 
        if kb.is_pressed("p"):
            break
        
    except:
        pass
