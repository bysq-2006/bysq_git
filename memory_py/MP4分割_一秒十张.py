import os
import cv2

def extract_frames(video_path, output_folder, num_frames=10):
    # 确保输出文件夹存在
    os.makedirs(output_folder, exist_ok=True)
    
    # 打开视频文件
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        raise ValueError(f"Unable to open video file: {video_path}")
    
    # 获取视频的总帧数
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # 计算每帧之间的间隔
    frame_interval = total_frames // num_frames
    
    frame_count = 0
    extracted_frames = 0
    
    while extracted_frames < num_frames:
        # 设置视频的当前位置
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_count)
        
        # 读取当前帧
        ret, frame = cap.read()
        
        if not ret:
            break
        
        # 保存当前帧
        frame_filename = os.path.join(output_folder, f"frame_{extracted_frames + 1}.jpg")
        cv2.imwrite(frame_filename, frame)
        
        frame_count += frame_interval
        extracted_frames += 1
    
    # 释放视频文件
    cap.release()

def process_videos_in_folder(input_folder, output_folder):
    # 确保输出文件夹存在
    os.makedirs(output_folder, exist_ok=True)
    
    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.mp4'):
            video_path = os.path.join(input_folder, filename)
            video_name = os.path.splitext(filename)[0]
            video_output_folder = os.path.join(output_folder, video_name)
            
            # 提取视频帧
            extract_frames(video_path, video_output_folder)

# 示例用法
input_folder = r"D:\bysq_D\mp4"
output_folder = r"D:\bysq_D\images"
process_videos_in_folder(input_folder, output_folder)
