from ultralytics import YOLO
import cv2, time, requests
import numpy as np
# import pyttsx3
# engine = pyttsx3.init()
url = r'http://47.113.146.59/pnggg/aaa.php'
yolo = YOLO(r"yolov8s.pt", task="detect")
start_time = time.time()

# 打开摄像头
cap = cv2.VideoCapture(0)
bai_image = np.ones((400, 400, 3), np.uint8) * 255
while True:
    # 读取一帧
    ret, frame = cap.read()
    if not ret:
        print("无法读取帧")
        break
    # 使用YOLO模型进行检测
    results = yolo(frame)# 遍历所有的检测结果
    for result in results:
        boxes = result.boxes.cpu().numpy()
        names = result.names  # 获取类别名称
        for box in boxes:
            r = box.xyxy[0].astype(int)  # 获取边界框坐标
            x1, y1, x2, y2 = r  # 解包坐标
            cls = int(box.cls[0])  # 获取类别索引
            conf = box.conf[0]  # 获取置信度
            
            # 只识别人类
            if names[cls] == "person":
                label = f"{names[cls]} {conf:.2f}"  # 创建标签文本
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 225), 2)
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    for result in results:
        person = 0
        boxes = result.boxes.cpu().numpy()
        for box in boxes:
            if box.cls == 0:
                person += 1
        current_time = time.time()
        # 检查是否已经过了3秒
        if current_time - start_time >= 3:
            if person > 0:
                is_success, buffer = cv2.imencode(".jpg", frame)
                if is_success:
                    # 构建文件上传的payload
                    files = {'image': ('image.jpg', buffer.tobytes(), 'image/jpeg')}
                    data = {'target_count': str(person)}

                    # 发送POST请求
                    response = requests.post(url, files=files, data=data)
            else:
                # 生成白色空白图片并上传
                is_success, buffer = cv2.imencode(".jpg", bai_image)
                if is_success:
                    files = {'image': ('0.jpg', buffer.tobytes(), 'image/jpeg')}
                    data = {'target_count': '0'}
                    response = requests.post(url, files=files, data=data)

            # engine.say("有" + str(person) + "个人在店里")
            # engine.runAndWait()
            start_time = current_time  # 重置开始时间
    # 检测按键事件
    if cv2.waitKey(1) & 0xFF == ord('m'):
        print("按下M键，退出循环")
        break

# 释放摄像头并关闭所有OpenCV窗口
cap.release()
cv2.destroyAllWindows()
