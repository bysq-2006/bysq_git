import pyautogui
import time

# 设置点击位置的坐标
x, y = 2246, 760  # 请根据需要修改为你的坐标

# 设置点击间隔时间（单位：秒）
interval = 1  # 每隔5秒点击一次


time.sleep(3)
try:
    while True:
        # 点击指定位置
        pyautogui.click(x, y)
        print(f"Clicked at ({x}, {y})")
        
        # 等待指定的间隔时间
        time.sleep(interval)

except KeyboardInterrupt:
    print("脚本已终止。")
