import os
import pyautogui
import random
import time
import keyboard
import webbrowser

run = True
url = ""  # url to chatgpt chat
path = ""  # path to screenshot file


def screenshot():
    screenshot = pyautogui.screenshot()
    string = "screenshots/" + (str)(random.randrange(10000, 99999)) + ".png"
    screenshot.save(string)
    put_in_chat_gpt()
    delete_screenshot(string)

def delete_screenshot(screenshot):
    if os.path.exists(screenshot):
        os.remove(screenshot)

def put_in_chat_gpt():
    bx, by = pyautogui.position()
    pyautogui.moveTo(-1007, 866) # click on the img upload
    pyautogui.leftClick()
    pyautogui.moveTo(-1273, 121) # click on the navigation bar
    pyautogui.leftClick()
    pyautogui.write(path)
    pyautogui.press('enter')
    pyautogui.moveTo(-1362, 235) # click on the newly made img
    pyautogui.doubleClick()
    time.sleep(1.5)
    pyautogui.moveTo(-295, 868) # submit the prompt
    pyautogui.leftClick()
    pyautogui.moveTo(bx, by) # move back to where you were before

def on_key_event(event):
    global run
    if event.name == 'l':
        screenshot()

    if event.name == 'p':
        run = False


keyboard.on_press(on_key_event)
webbrowser.open_new_tab(url)
while run:
    time.sleep(1)

