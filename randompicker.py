import keyboard
import pyautogui as pg
import time
import random
print('File has initialized')
#reads the text files first line and gets the x and y
cords=['582 923','667 923','750 923','831 923','918 923','1003 923','1084 923','1169 923','1253 923','1336 923','582 1006','667 1006','750 1006','831 1006','918 1006','1003 1006','1084 1006','1169 1006','1253 1006','1336 1006',]
line=cords[random.randint(0,len(cords))]
print(line)
line=line.split()
x=int(line[0])
y=int(line[1])
[]
'''
The defaults are:
astra or 1st button - 582 923
breach or 2nd button - 667 923
brim or 3rd button - 750 923
chamber 4th button - 831 923
cypher or 5th button - 918 923
fade or 6th button - 1003 923
jett or 7th button - 1084 923
kayo or 8th button - 1169 923
kj or 9th button - 1253 923
neon or 10th button - 1336 923
omen or 11th button - 582 1006
phoenix or 12th button - 667 1006
raze or 13th button - 750 1006
reyna or 14th button - 831 1006
sage or 15th button - 918 1006
skye or 16th button - 1003 1006
sova or 17th button - 1084 1006
viper or 18th button - 1169 1006
yoru or 19th button - 1253 1006
'''
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