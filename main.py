import pyautogui
import time
import datetime
import webbrowser as wb

screen_width, screen_height = pyautogui.size()

wb.open("https://instagram.com")

# Variables page 1
profile_click_x, profile_click_y = 427, 0
instagram_profile_icon_x, instagram_profile_icon_y = 1173, 142
switch_accounts_x, switch_accounts_y = 1089, 296
login_existing_accounts_x, login_existing_accounts_y = 716, 596
login_x, login_y = 708, 494
passwrd_x, passwrd_y = 693, 539
press_login_x, press_login_y = 719, 615

# Variables page 2,3,4,5
username_button_x, username_button_y = 893, 323
psswrd_button_x, psswrd_button_y = 926, 365
login_button_x, login_button_y = 918, 411

# Profiles positions
account_03_x, account_03_y = 445, 307

# Account 1
time.sleep(8)
pyautogui.moveTo(instagram_profile_icon_x, instagram_profile_icon_y)
time.sleep(1)
pyautogui.click()
pyautogui.moveTo(switch_accounts_x, switch_accounts_y) # Switching accounts
time.sleep(1.3)
pyautogui.click()
pyautogui.moveTo(login_existing_accounts_x, login_existing_accounts_y) # login in existing accounts
time.sleep(1.5)
pyautogui.click()
pyautogui.moveTo(login_x, login_y) # login
pyautogui.click()
time.sleep(0.7)
pyautogui.write('') # username
pyautogui.moveTo(passwrd_x, passwrd_y)
pyautogui.click()
time.sleep(0.3)
pyautogui.click()
time.sleep(1)
pyautogui.write('') # password
pyautogui.moveTo(press_login_x, press_login_y) # login
time.sleep(0.8)
pyautogui.click()
time.sleep(1)

# account 2
pyautogui.hotkey('command', 'shift', 'n')
time.sleep(1)
pyautogui.write('instagram.com')
pyautogui.press('enter')
time.sleep(5)
pyautogui.moveTo(username_button_x, username_button_y)
pyautogui.click()
time.sleep(0.6)
pyautogui.write('')#username goes here
pyautogui.moveTo(psswrd_button_x, psswrd_button_y)
pyautogui.click()
time.sleep(0.3)
pyautogui.click()
pyautogui.write('') # password
pyautogui.moveTo(login_button_x, login_button_y)
time.sleep(0.5)
pyautogui.click()
time.sleep(0.8)

# account 3
pyautogui.moveTo(profile_click_x, profile_click_y)
time.sleep(1)
pyautogui.click()
time.sleep(1)
pyautogui.moveTo(account_03_x, account_03_y)
time.sleep(0.6)
pyautogui.click()
time.sleep(1)
pyautogui.write('instagram.com')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.3)
pyautogui.hotkey('command', 'shift', 'n')
time.sleep(0.3)

# account 4
pyautogui.write('instagram.com')
pyautogui.press('enter')
time.sleep(5)
pyautogui.moveTo(username_button_x, username_button_y)
pyautogui.click()
pyautogui.write('') #username goes here
pyautogui.moveTo(psswrd_button_x, psswrd_button_y)
pyautogui.click()
time.sleep(0.3)
pyautogui.click()
pyautogui.write('') # password
pyautogui.moveTo(login_button_x, login_button_y)
time.sleep(0.5)
pyautogui.click()






