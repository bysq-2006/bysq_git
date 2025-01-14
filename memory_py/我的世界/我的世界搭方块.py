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

# 设置总次数
total_iterations = 2#-----------------------------------------------------------------------------------------------------

stop_flag = False

def stop_operation():
    global stop_flag
    keyboard.wait('q')  # 等待按下 'Q' 键
    stop_flag = True
    engine.say("操作已取消")  # 播报取消操作
    engine.runAndWait()

# 启动一个线程来监听键盘事件
threading.Thread(target=stop_operation, daemon=True).start()

inventory = 2  #物品栏
for iteration in range(total_iterations):
    if stop_flag:  # 检查是否需要停止操作
        break

    # 模拟按住 Shift + S
    pyautogui.keyDown('shift')  # 按住 Shift 键
    pyautogui.keyDown('s')      # 按住 S 键

    # 模拟按住鼠标右键
    pyautogui.mouseDown(button='right')  # 按住鼠标右键

    # 保持按住状态 52 秒
    time.sleep(52)

    if stop_flag:  # 检查是否需要停止操作
        break

    pyautogui.keyDown(f"{inventory}")
    pyautogui.keyUp(f"{inventory}")
    inventory += 1  # 物品栏自增

    # 松开鼠标右键
    pyautogui.mouseUp(button='right')  # 松开鼠标右键

    # 松开 S 键和 Shift 键
    pyautogui.keyUp('s')      # 松开 S 键
    # 可选：在每次迭代之间休息一下，可以调整时间
    time.sleep(1)
    pyautogui.keyUp('shift')  # 松开 Shift 键

    # 播报完成当前循环
    engine.say(f"第 {iteration + 1} 次操作完成")
    engine.runAndWait()


# 最后给一个提示，表示完成全部任务
if not stop_flag:  # 确保不是因为按下 "Q" 键停止的
    engine.say("所有操作完成")
    engine.runAndWait()
