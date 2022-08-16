import keyboard
import pyautogui as pg
import time
print('File has initialized')
#reads the text files first line and gets the x and y
with open("coordinates.txt") as file:firstline=file.read().split('\n',1)[0].split()
x=int(firstline[0])
y=int(firstline[1])
while True:
    if keyboard.is_pressed("g"):
        print("the location is: "+str(pg.position()).replace('Point(',"").replace(', ',"").replace(')',"").replace('y='," ").replace('x=',""))
    if keyboard.is_pressed("c"):
        print("the agent has been selected")

        #clicks the agent
        pg.click(x, y, button="left");time.sleep(0.1)

        #confirms the agent
        pg.click(957, 812, button="left") #press twice just because
        pg.click(957, 812, button="left");time.sleep(0.1)
    if keyboard.is_pressed("e"):
        print("File closed")
        break
