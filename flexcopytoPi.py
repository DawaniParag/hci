import pyautogui
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)
i = GPIO.input(4)
if(i==1):
    pyautogui.mouseDown(button='left')
else:
     pyautogui.mouseUp(button='left')
    
