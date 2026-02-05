import pyautogui
import time

user_loc = input("이미지 파일 위치: ")

while True:
    try:
        button = pyautogui.locateOnScreen(user_loc, confidence=0.9)
        if button:
            x, y = pyautogui.center(button)
            pyautogui.click(x, y)
            time.sleep(0.1)
    except pyautogui.ImageNotFoundException:
        pass
