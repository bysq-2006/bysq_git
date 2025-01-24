from moviepy.editor import VideoFileClip

def extract_frame(video_path, output_path, frame_number=0):
    """
    从视频中提取指定帧并保存为图片

    :param video_path: 视频文件路径
    :param output_path: 输出图片路径
    :param frame_number: 要提取的帧号，默认为0，即第一帧
    """
    # 加载视频文件
    video = VideoFileClip(video_path)
    
    # 提取指定帧
    frame = video.get_frame(frame_number)
    
    # 保存为图片
    video.save_frame(output_path, t=frame_number / video.fps)
    
    print(f"帧已成功提取并保存到 {output_path}")

# 示例使用
video_path = r'D:\bysq\mmexport1579195022764.mp4'
output_path = r'D:\bysq\linlin.png'
extract_frame(video_path, output_path)
