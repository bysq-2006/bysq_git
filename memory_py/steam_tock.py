import pyautogui
import time
import keyboard  # 导入keyboard库

# 设置点击位置的坐标

# 设置点击间隔时间（单位：秒）
interval = 1  # 每隔1秒点击一次

time.sleep(4)
x, y = pyautogui.position()
try:
    while True:
        # 检测是否按下 'c' 键
        if keyboard.is_pressed('c'):
            print("检测到 'c' 键，脚本将终止。")
            break
        
        # 点击指定位置
        pyautogui.click(x, y)
        print(f"Clicked at ({x}, {y})")
        
        # 等待指定的间隔时间
        time.sleep(interval)

except KeyboardInterrupt:
    print("脚本已终止。")
