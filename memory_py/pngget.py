import cv2
import keyboard
import time

# 打开摄像头
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("无法打开摄像头")
    exit()

print("按 'P' 键截取图片，按 'Q' 键退出。")
i = 0
while True:
    # 逐帧捕获
    ret, frame = cap.read()
    
    if not ret:
        print("无法读取图像")
        break

    # 显示当前帧
    cv2.imshow('Camera', frame)
    cv2.waitKey(1)
    # 监听键盘事件
    if keyboard.is_pressed('p'):  # 如果按下 'P' 键
        time.sleep(0.1)  # 等待1秒
        cv2.imwrite(f'{i}.png', frame)  # 保存图片
        print(f"图片已保存为 '{i}.png'")
        i += 1  # 增加图片编号

    if keyboard.is_pressed('q'):  # 如果按下 'Q' 键
        print("退出程序")
        break

# 释放摄像头并关闭所有窗口
cap.release()
cv2.destroyAllWindows()
