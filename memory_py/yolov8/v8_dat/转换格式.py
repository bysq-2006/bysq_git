import os
import glob
import json

def read_json_files(folder_path):
    if not os.path.exists(r"./point"):
        os.makedirs(r"./point")
    # 使用glob模块查找所有.json文件
    json_files = glob.glob(os.path.join(folder_path, '*.json'))
    
    for file_path in json_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                a1, a2, a3, a4, a5 = None, None, None, None, None
                data = json.load(file)
                print(f"读取文件: {file_path}")
                # print(data)
            if data['shapes'][0]['label'] == "香橙派":
                a1 = "0"
            x1 = data['shapes'][0]['points'][0][0]
            x2 = data['shapes'][0]['points'][2][0]
            a2 = ((x1+x2)/2)/data['imageWidth']
            y1 = data['shapes'][0]['points'][0][1]
            y2 = data['shapes'][0]['points'][2][1]
            a3 = ((y1+y2)/2)/data['imageHeight']
            a4 = (x2-x1)/data['imageWidth']
            a5 = (y2-y1)/data['imageHeight']
            filename = os.path.basename(file_path)
            filename = filename[:-5]
        except PermissionError:
            print(f"无法读取文件 {file_path}: 权限错误")
        except json.JSONDecodeError:
            print(f"无法解析文件 {file_path}: JSON 格式错误")
        except Exception as e:
            print(f"读取文件 {file_path} 时发生错误: {e}")
        with open(f"./point/{filename}.txt", "w", encoding='utf-8') as f:
            # os.chmod(r"./point", 0o666)
            f.write(f"{a1} {a2} {a3} {a4} {a5}")

# 示例调用
folder_path = r'C:\bysq\v8_dat'  # 使用原始字符串避免转义字符问题
read_json_files(folder_path)
