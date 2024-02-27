import pyautogui as pg
from time import sleep
import webbrowser
import pyperclip as pc

file = open("G:\\My Drive\\MyProjects\\Python\\GadgetsInsta\\counter.txt","r")
count = int(file.read().strip())
file.close()
print(pg.position())
exit()


caption = "Diving into the future with the latest trending gadget! 🚀🔥 Swipe to witness the tech revolution. 💡 Don't miss out - stay updated with the coolest tech trends! 💻📱 Remember to like, share, and follow @techbuzzwave for more amazing tech content! 🤖✨ #TrendingTech #InnovationNation #GadgetGoals"
pc.copy(caption)

webbrowser.open_new_tab(f"https://www.instagram.com/")
sleep(10)
pg.click(88,601)
sleep(5)
pg.click(944,672)
sleep(5)
pg.typewrite(f"vdo ({count}).mp4",0.07)
pg.press("enter")
sleep(5)
pg.click(609,945)
sleep(1)
pg.click(641,743)
sleep(1)
pg.click(1297,209)
sleep(3)
pg.click(1468,208)
sleep(2)
pg.click(1310,363)
sleep(1)
pg.hotkey("ctrl","v")
sleep(1)
pg.click(1461,211)
sleep(2)

file = open("G:\\My Drive\\MyProjects\\Python\\GadgetsInsta\\counter.txt","w")
count += 1
file.write(f"{count}")
file.close()
sleep()