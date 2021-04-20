import pyautogui
import time
import datetime
import webbrowser as wb

screen_width, screen_height = pyautogui.size()

wb.open("https://instagram.com")

time.sleep(10)
instagram_profile_icon_x, instagram_profile_icon_y = 1173, 142
pyautogui.moveTo(instagram_profile_icon_x, instagram_profile_icon_y)
time.sleep(1)
pyautogui.click()
switch_accounts_x, switch_accounts_y = 1089, 296
pyautogui.moveTo(switch_accounts_x, switch_accounts_y)
time.sleep(1.3)
pyautogui.click()




#profile_click_x, profile_click_y = 431, 0
#pyautogui.moveTo(profile_click_x, profile_click_y)
#time.sleep(1)
#pyautogui.click()

