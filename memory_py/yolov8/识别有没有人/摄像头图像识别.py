from ultralytics import YOLO
import cv2

# 加载YOLO模型
yolo = YOLO(r"C:\bysq\memory_py\yolov8n.pt", task="detect")

# 打开摄像头
cap = cv2.VideoCapture(0)

while True:
    # 读取一帧
    ret, frame = cap.read()
    if not ret:
        break

    # 使用YOLO模型进行检测
    results = yolo(frame)

    # 遍历所有的检测结果
    for result in results:
        boxes = result.boxes.cpu().numpy()
        names = result.names  # 获取类别名称
        for box in boxes:
            r = box.xyxy[0].astype(int)  # 获取边界框坐标
            x1, y1, x2, y2 = r  # 解包坐标
            cls = int(box.cls[0])  # 获取类别索引
            conf = box.conf[0]  # 获取置信度
            label = f"{names[cls]} {conf:.2f}"  # 创建标签文本
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 225), 2)
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.namedWindow('Image Display', cv2.WINDOW_NORMAL)
    # cv2.imshow('Image Display', frame)

    # 显示检测结果
    cv2.imshow('YOLO Detection', frame)

    # 按 'q' 键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头并关闭窗口
cap.release()
cv2.destroyAllWindows()
