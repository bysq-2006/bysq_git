import pyautogui
import time
import pyttsx3
import threading
import keyboard
engine = pyttsx3.init()

# 设置倒计时时间（例如5秒）
countdown_time = 2

# 语音倒计时
for i in range(countdown_time, 0, -1):
    engine.say(f"{i}")
    engine.runAndWait()
    time.sleep(1)

sum = 600

for i in range(sum):
    pyautogui.mouseDown(button='left')  # 松开鼠标右键
    pyautogui.mouseUp(button='left')  # 松开鼠标右键
    time.sleep(0.43)  # 延时0.1秒