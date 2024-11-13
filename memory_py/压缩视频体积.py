from moviepy.editor import VideoFileClip

def compress_video(input_file, output_file, target_size):
    # 打开视频文件
    video = VideoFileClip(input_file)
    
    # 获取视频时长（秒）
    duration = video.duration
    
    # 计算目标比特率
    # 1GB ≈ 1024*1024 KB, 所以目标大小是 300MB = 300*1024 KB
    target_bitrate = (target_size * 1024 * 1024 * 8) / duration  # 单位为 bps (比特/秒)

    # 将比特率转换为 kbps
    target_bitrate_kbps = int(target_bitrate / 1000)
    
    # 设置新的视频编码参数
    video.write_videofile(output_file, bitrate=f"{target_bitrate_kbps}k", codec="libx264", audio_bitrate="192k")

# 使用示例
input_video_path = r"C:\bysq\memory_py\NARAKA  BLADEPOINT 2024.10.03 - 22.04.20.01.mp4"  # 输入视频文件路径
output_video_path = r"output_video.mp4"  # 输出视频文件路径
target_size_mb = 300  # 目标压缩到300MB

compress_video(input_video_path, output_video_path, target_size_mb)
