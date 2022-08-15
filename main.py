import keyboard
import pyautogui as pg
import time

#change these values to the agent you want
x=1164
y=918

while True:
    if keyboard.is_pressed("g"):
        print("the location is: "+str(pg.position()).replace('Point(x',"").replace(', ',"").replace(')',""))
    if keyboard.is_pressed("c"):
        print("the agent has been selected")

        #clicks the agent
        pg.click(x, y, button="left");time.sleep(0.01)

        #confirms the agent
        pg.click(903, 785, button="left");time.sleep(0.01)
    if keyboard.is_pressed("e"):
        break

