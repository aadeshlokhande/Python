# pip install pyautogui

# AUTOMATION

# selenium - web

# pyautogui



# mouse 
# click 
# double click
# right click
# scroll 
# move 
# drag 





# ===================================


# import pyautogui 

# a = pyautogui.position()
# print(a)

# pyautogui.moveTo(604,1057,3)
# pyautogui.click(604,1057)
# pyautogui.doubleClick(604,1057)
# pyautogui.rightClick(604,1057)
# pyautogui.drag(604,1057)
# pyautogui.scroll(10000)

# pyautogui.move(100,100,3)

# **************************
# keyboard
# keys press 
# typing 
# shortcut keys 

# pyautogui.press("esc")
# pyautogui.typewrite("hello pragati kashi ahe",0.08)
# pyautogui.hotkey('ctrl','a')


#########################################
# import time 
# import pyautogui 

# time.sleep(2)
# # a = pyautogui.position()
# # print(a)
# # exit()
# pyautogui.click(1054,1069)
# time.sleep(4)
# pyautogui.click(254,119)
# pyautogui.typewrite("Pragati Choudhary",0.1)
# time.sleep(3)
# pyautogui.click(216,187)
# time.sleep(1)
# pyautogui.typewrite("Hello pragati... jewlis ka w",0.1)
# pyautogui.press("enter")


# =======================================

import pyautogui as pg 
import time 
for i in range(20):
    try:
        x,y = pg.locateCenterOnScreen("LIKE.png")
        pg.click(x,y)
        time.sleep(1)
    except:
        pg.scroll(-2000)
        time.sleep(1)
