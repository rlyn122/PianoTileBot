import pyautogui
import keyboard
import time
import win32api, win32con

# Four positions for four lanes
#played on https://lagged.com/en/g/magic-tiles


buf=0
#pixel positions of black squares on screen (changes depending on device)
x1=788
y=582
x2=898
x3=1000
x4=1117

start1=0
start2=0
start3=0
start4=0
t=0

def ClickOn(X,Y): #This function clicks on position x,y
    win32api.SetCursorPos((X,Y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
 

def TakeyTimey(X,Y,start): #function tracks the speed black squares pass by at
    if pyautogui.pixel(X,Y) == (0,0,0) and start==0:
            start=time.time()
    
    if pyautogui.pixel(X,Y) != (0,0,0) and start!=0:
            t=time.time()-start
            print(t)
            start=0


while keyboard.is_pressed(' ') == False:



    if pyautogui.pixel(x1,y)[0] == 0:   
        ClickOn(x1,y+buf)

    if pyautogui.pixel(x2,y)[0] == 0:    
        ClickOn(x2,y+buf)

    if pyautogui.pixel(x3,y)[0] == 0:    
        ClickOn(x3,y+buf)

    if pyautogui.pixel(x4,y)[0] == 0:    
        ClickOn(x4,y+buf)

    #TakeyTimey(518,575,start1)
    #TakeyTimey(624,575,start2)
    #TakeyTimey(724,575,start3)
    #TakeyTimey(828,575,start4)

    
    #print(pyautogui.position()) 

 
