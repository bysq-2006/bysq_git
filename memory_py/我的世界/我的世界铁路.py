import pyautogui 
import time
import pyttsx3
import threading
import keyboard

# 初始化语音引擎
engine = pyttsx3.init()

# 设置倒计时时间（例如5秒）
countdown_time = 2

# 语音倒计时
for i in range(countdown_time, 0, -1):
    engine.say(f"{i}")
    engine.runAndWait()
    time.sleep(1)

num = 1
sum = 0

total_count = 150  # 设置总次数-------------------------------------------------------------------------------------------------------------
distant = 9  #每隔几格放一个动力铁轨

inventory = 2  #物品栏---这一栏不可以动
pyautogui.keyDown('shift')  # 按下'W'键

for _ in range(total_count):
    if sum == 64:  # 达到64个铁轨时停止
        sum = 0
        inventory += 1
        pyautogui.scroll(-115)  # 向下滚动（负值表示向下）
    sum += 1

    if (num + distant) % distant == 0:#放置动力铁轨和红石火把
        num = 1
        pyautogui.keyDown("1")
        pyautogui.keyUp("1")
        pyautogui.keyDown("space")
        time.sleep(0.05)
        pyautogui.keyUp("space")
        pyautogui.mouseDown(button='right')  # 按住鼠标右键
        pyautogui.mouseUp(button='right')  # 松开鼠标右键
        pyautogui.keyDown("s")
        time.sleep(0.34 )
        pyautogui.keyUp("s")
        # 放置红石火把
        pyautogui.keyDown("9")
        pyautogui.keyUp("9")
        pyautogui.mouseDown(button='right')  # 按住鼠标右键
        pyautogui.mouseUp(button='right')  # 松开鼠标右键
        pyautogui.keyDown("8")
        pyautogui.keyUp("8")
        pyautogui.mouseDown(button='right')  # 按住鼠标右键
        pyautogui.mouseUp(button='right')  # 松开鼠标右键
        pyautogui.keyDown("w")
        time.sleep(0.25)
        pyautogui.keyUp("w")

    else:#放置普通铁轨
        num += 1
        pyautogui.keyDown(f"{inventory}")
        pyautogui.keyUp(f"{inventory}")
        pyautogui.keyDown("space")
        time.sleep(0.05)
        pyautogui.keyUp("space")
        pyautogui.mouseDown(button='right')  # 按住鼠标右键
        time.sleep(0.05)
        pyautogui.mouseUp(button='right')  # 松开鼠标右键
    pyautogui.keyDown('d')  # 按下'W'键

    time.sleep(0.683 )  # 等待

    pyautogui.keyUp('d')  # 松开'W'键 

pyautogui.keyUp('shift')  # 松开'W'键2