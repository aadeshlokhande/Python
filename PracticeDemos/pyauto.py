# # pyautogui
# # pip install pyautogui

# from time import sleep
# import pyautogui

# a = pyautogui.position()
# print(a)

# # sleep()

# # keyboard
# # type 
# pyautogui.typewrite("str")

# # shortcut
# pyautogui.hotkey("ctrl","a")

# # press 
# pyautogui.press("enter")

# # mouse

# # click
# pyautogui.click(1000,10)
# # double click
# pyautogui.doubleClick(400,400)

# # right click
# pyautogui.rightClick(1000,500)

# # scroll
# pyautogui.scroll(1200)

# # drag 
# pyautogui.drag(120,430)

# # move 
# pyautogui.move(192,700)

# ======================================================


from time import sleep
import pyautogui

# a = pyautogui.position()
# print(a)

name = input("enter a name = ")

pyautogui.press("win")
sleep(1)
pyautogui.typewrite("Whatsapp",0.07)
pyautogui.press("enter")
sleep(3)
pyautogui.click(295,121)
pyautogui.typewrite(name,0.09)
sleep(5)
pyautogui.click(219,191)
sleep(2)
pyautogui.typewrite("*Hello*",0.1)
pyautogui.press("enter")
