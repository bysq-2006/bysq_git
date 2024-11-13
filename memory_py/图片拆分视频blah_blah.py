import os
import cv2
import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import threading
import shutil
import webbrowser
import re

def extract_frames(video_path, output_folder, output_format='jpg', frames_per_second=10, progress_callback=None):
    os.makedirs(output_folder, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        raise ValueError(f"无法打开视频文件: {video_path}")
    
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_interval = int(fps / frames_per_second)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    frame_count = 0
    extracted_frames = 0
    
    while True:
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_count)
        ret, frame = cap.read()
        
        if not ret:
            break
        
        frame_filename = os.path.join(output_folder, f"frame_{extracted_frames + 1}.{output_format}")
        cv2.imwrite(frame_filename, frame)
        
        frame_count += frame_interval
        extracted_frames += 1
        
        if progress_callback:
            progress_callback(extracted_frames * frame_interval / total_frames * 100)
    
    while extracted_frames < frames_per_second:
        src_frame = os.path.join(output_folder, f"frame_{extracted_frames % (frames_per_second - 1) + 1}.{output_format}")
        dst_frame = os.path.join(output_folder, f"frame_{extracted_frames + 1}.{output_format}")
        shutil.copy(src_frame, dst_frame)
        extracted_frames += 1
    
    cap.release()

def convert_to_mp4(input_path, output_path):
    command = f"ffmpeg -i {input_path} -c:v libx264 -c:a aac {output_path}"
    subprocess.call(command, shell=True)

def process_single_video(input_path, output_folder, output_format='jpg', frames_per_second=10, progress_callback=None):
    os.makedirs(output_folder, exist_ok=True)
    video_name = os.path.splitext(os.path.basename(input_path))[0]
    video_output_folder = os.path.join(output_folder, video_name)
    extract_frames(input_path, video_output_folder, output_format, frames_per_second, progress_callback)

def select_input_file():
    file_selected = filedialog.askopenfilename()
    input_file_path.set(file_selected)

def select_output_folder():
    folder_selected = filedialog.askdirectory()
    output_folder_path.set(folder_selected)

def start_processing():
    input_path = input_file_path.get()
    output_path = output_folder_path.get()
    output_format = output_format_var.get()
    frames_per_second = int(frames_per_second_var.get())
    
    if input_path and output_path:
        def update_progress(percentage):
            if percentage == 0:
                progress_var.set("程序未开始")
            else:
                progress_var.set(f"进度: {percentage:.2f}%")
        
        def process_video():
            try:
                process_single_video(input_path, output_path, output_format, frames_per_second, update_progress)
                messagebox.showinfo("完成", "视频处理完成！")
            except Exception as e:
                messagebox.showerror("中途关闭了程序\n或者发生了错误", f"处理视频时出错: {e}")
            finally:
                start_button.config(state=tk.NORMAL)
                start_button.grid(row=5, column=0, columnspan=3, pady=20)
                processing_label.grid_remove()
        
        start_button.config(state=tk.DISABLED)
        start_button.grid_remove()
        processing_label.grid(row=5, column=0, columnspan=3, pady=20)
        
        threading.Thread(target=process_video).start()
    else:
        messagebox.showwarning("警告", "请选择输入文件和输出文件夹！")

def start_video_to_images():
    root.destroy()
    run_video_to_images_program()

def run_video_to_images_program():
    global input_file_path, output_folder_path, output_format_var, frames_per_second_var, progress_var, start_button, processing_label

    root = tk.Tk()
    root.title("视频帧提取器")

    input_file_path = tk.StringVar()
    tk.Label(root, text="输入文件:").grid(row=0, column=0, padx=10, pady=5)
    tk.Entry(root, textvariable=input_file_path, width=50).grid(row=0, column=1, padx=10, pady=5)
    tk.Button(root, text="选择", command=select_input_file).grid(row=0, column=2, padx=10, pady=5)

    output_folder_path = tk.StringVar()
    tk.Label(root, text="输出文件夹:").grid(row=1, column=0, padx=10, pady=5)
    tk.Entry(root, textvariable=output_folder_path, width=50).grid(row=1, column=1, padx=10, pady=5)
    tk.Button(root, text="选择", command=select_output_folder).grid(row=1, column=2, padx=10, pady=5)

    output_format_var = tk.StringVar(value='jpg')
    tk.Label(root, text="输出格式:").grid(row=2, column=0, padx=10, pady=5)
    tk.OptionMenu(root, output_format_var, 'jpg', 'png').grid(row=2, column=1, padx=10, pady=5)

    frames_per_second_var = tk.StringVar(value='24')
    tk.Label(root, text="每秒帧数:").grid(row=3, column=0, padx=10, pady=5)
    tk.Entry(root, textvariable=frames_per_second_var, width=20).grid(row=3, column=1, padx=10, pady=5)

    progress_var = tk.StringVar(value="程序未开始")
    tk.Label(root, textvariable=progress_var).grid(row=4, column=0, columnspan=3, padx=10, pady=5)

    start_button = tk.Button(root, text="开始处理", command=start_processing)
    start_button.grid(row=5, column=0, columnspan=3, pady=20)

    processing_label = tk.Label(root, text="程序已经开始")

    root.mainloop()

def start_images_to_video():
    root.destroy()
    run_images_to_video_program()

def run_images_to_video_program():
    global input_folder_path, output_file_path, frames_per_second_var, progress_var, start_button, processing_label

    root = tk.Tk()
    root.title("图片合成视频")

    input_folder_path = tk.StringVar()
    tk.Label(root, text="输入文件夹:").grid(row=0, column=0, padx=10, pady=5)
    tk.Entry(root, textvariable=input_folder_path, width=50).grid(row=0, column=1, padx=10, pady=5)
    tk.Button(root, text="选择", command=lambda: input_folder_path.set(filedialog.askdirectory())).grid(row=0, column=2, padx=10, pady=5)

    output_file_path = tk.StringVar()
    tk.Label(root, text="输出文件:").grid(row=1, column=0, padx=10, pady=5)
    tk.Entry(root, textvariable=output_file_path, width=50).grid(row=1, column=1, padx=10, pady=5)
    tk.Button(root, text="选择", command=lambda: output_file_path.set(filedialog.asksaveasfilename(defaultextension=".mp4"))).grid(row=1, column=2, padx=10, pady=5)

    frames_per_second_var = tk.StringVar(value='24')
    tk.Label(root, text="每秒帧数:").grid(row=2, column=0, padx=10, pady=5)
    tk.Entry(root, textvariable=frames_per_second_var, width=20).grid(row=2, column=1, padx=10, pady=5)

    progress_var = tk.StringVar(value="程序未开始")
    tk.Label(root, textvariable=progress_var).grid(row=3, column=0, columnspan=3, padx=10, pady=5)

    def start_processing():
        input_path = input_folder_path.get()
        output_path = output_file_path.get()
        frames_per_second = int(frames_per_second_var.get())
        
        if input_path and output_path:
            def update_progress(percentage):
                if percentage == 0:
                    progress_var.set("程序未开始")
                else:
                    progress_var.set(f"进度: {percentage:.2f}%")
            
            def process_images():
                try:
                    combine_images_to_video(input_path, output_path, frames_per_second, update_progress)
                    messagebox.showinfo("完成", "视频合成完成！")
                except Exception as e:
                    messagebox.showerror("错误", f"合成视频时出错: {e}")
                finally:
                    start_button.config(state=tk.NORMAL)
                    start_button.grid(row=4, column=0, columnspan=3, pady=20)
                    processing_label.grid_remove()
            
            start_button.config(state=tk.DISABLED)
            start_button.grid_remove()
            processing_label.grid(row=4, column=0, columnspan=3, pady=20)
            
            threading.Thread(target=process_images).start()
        else:
            messagebox.showwarning("警告", "请选择输入文件夹和输出文件！")

    start_button = tk.Button(root, text="开始处理", command=start_processing)
    start_button.grid(row=4, column=0, columnspan=3, pady=20)

    processing_label = tk.Label(root, text="程序已经开始")

    root.mainloop()

def combine_images_to_video(input_folder, output_path, frames_per_second=24, progress_callback=None):
    messagebox.showinfo("提示", "请将图片(图片的名字比如1.jpg)排好序并且按照从小到大的顺序放入文件夹\n程序即将开始")
    
    images = [img for img in os.listdir(input_folder) if img.endswith(".jpg") or img.endswith(".png")]
    
    def extract_number(filename):
        match = re.search(r'\d+', filename)
        return int(match.group()) if match else 0
    
    images.sort(key=extract_number)
    
    if len(images) == 0:
        raise ValueError("输入文件夹中没有找到图片")
    
    frame = cv2.imread(os.path.join(input_folder, images[0]))
    height, width, layers = frame.shape
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(output_path, fourcc, frames_per_second, (width, height))
    
    total_images = len(images)
    for i, image in enumerate(images):
        img_path = os.path.join(input_folder, image)
        frame = cv2.imread(img_path)
        video.write(frame)
        
        if progress_callback:
            progress_callback((i + 1) / total_images * 100)
    
    video.release()

def open_author_page():
    webbrowser.open("https://space.bilibili.com/361744550?spm_id_from=333.788.0.0")

root = tk.Tk()
root.title("视频处理工具")

tk.Button(root, text="视频分割成图片", command=start_video_to_images).grid(row=0, column=0, padx=10, pady=20)
tk.Button(root, text="图片合成视频", command=start_images_to_video).grid(row=0, column=1, padx=10, pady=20)
tk.Button(root, text="作者", command=open_author_page).grid(row=0, column=2, padx=10, pady=20)

root.mainloop()
