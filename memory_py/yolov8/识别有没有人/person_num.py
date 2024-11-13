from ultralytics import YOLO
import cv2
import os
import time
import numpy as np

# 创建目录
if not os.path.isdir('person_num/'):
    os.mkdir("person_num/")

# 加载模型
model = YOLO(r'D:\bysq\yolov8s.pt')  # 使用绝对路径
image_path = 'person_num/start.png'

while True:
    time.sleep(1)
    if os.path.isfile(image_path):  # 检测文件是否存在
        # 读取图像并压缩到720p
        # 读取图像并压缩到1080p
        image = cv2.imread(image_path)
        height, width = image.shape[:2]
        if height > 1080 or width > 1920:
            aspect_ratio = width / height
            if aspect_ratio > 1920 / 1080:
                new_width = 1920
                new_height = int(1920 / aspect_ratio)
            else:
                new_height = 1080
                new_width = int(1080 * aspect_ratio)
            image = cv2.resize(image, (new_width, new_height))

        # 创建一个白色的背景
        white_background = 255 * np.ones(shape=image.shape, dtype=np.uint8)

        # 将图像放在白色背景上
        y_offset = (white_background.shape[0] - image.shape[0]) // 2
        x_offset = (white_background.shape[1] - image.shape[1]) // 2
        white_background[y_offset:y_offset + image.shape[0], x_offset:x_offset + image.shape[1]] = image

        # 进行模型预测
        results = model.predict(white_background)
        person_count = 0
        for result in results:
            boxes = result.boxes  # 获取检测的边界框信息
            if boxes is not None:
                person_count = 0
                for box in boxes:
                    # box.xyxy 是边界框的坐标，box.conf 是置信度，box.cls 是类
                    x1, y1, x2, y2 = map(int, box.xyxy[0])  # 边界框坐标
                    conf = box.conf[0]                       # 置信度
                    cls = int(box.cls[0])                    # 类别
                    if cls == 0:  # 假设类别 0 是人
                        person_count += 1
                        # 绘制边框（红色）
                        cv2.rectangle(white_background, (x1 + x_offset, y1 + y_offset), 
                                      (x2 + x_offset, y2 + y_offset), (0, 0, 255), 2)  # 红色边框

        # 计算文本大小为边框大小的1/10
        if person_count > 0:
            # 选取第一个边框来计算大小
            first_box = boxes[0]
            new_width = int(first_box.xyxy[0][2] - first_box.xyxy[0][0])
            new_height = int(first_box.xyxy[0][3] - first_box.xyxy[0][1])
            font_scale = min(width, height) / 200  # 根据边框大小设置文本大小

            # 在图像中央顶部绘制人数和边框
            text = f"preson_num: {person_count}"
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_thickness = 2
            text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
            text_x = (white_background.shape[1] - text_size[0]) // 2
            text_y = 50  # 在顶部的 y 坐标

            # 在矩形上绘制黑色文本
            cv2.putText(white_background, text, (text_x, text_y), font, font_scale, (0, 0, 0), font_thickness)  # 黑色字体

        # 保存结果图像
        cv2.imwrite('person_num/end.png', white_background)

        # 删除原始图像
        os.remove(image_path)

        print(f"检测到的人数: {person_count}")
    else:
        print(f"文件 {image_path} 不存在，跳过该步骤。")
