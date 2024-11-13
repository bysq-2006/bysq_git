from ultralytics import YOLO
import os

if __name__ == "__main__":
    os.environ['CUDA_VISIBLE_DEVICES'] = '0'
    # import torch
    # print(torch.cuda.is_available())

    # 加载预训练的 YOLOv8 模型
    model = YOLO(r"C:\bysq\memory_py\yolov8n.pt")

    # 定义数据配置文件路径
    data_config_path = r"C:\bysq\v8_dat\123.yaml"
    # 训练模型
    model.train(
        data=data_config_path,  # 数据配置文件路径
        epochs=100,             # 训练的轮数
        device="0"              # 使用的设备，"0" 表示使用 GPU，"cpu" 表示使用 CPU
    )
