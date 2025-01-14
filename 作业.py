import random
import matplotlib.pyplot as plt
import matplotlib

# 设置字体以显示中文
matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 设置无衬线字体
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号 '-' 显示为方块的问题

# 初始化统计数组
# 均值的范围是1到60，差值的范围是0到59
mean_counts = [0] * 60  # 均值从1到60
diff_counts = [0] * 60  # 差值从0到59

# 执行十万次随机取两个点
for _ in range(100000):
    a = random.randint(1, 60)
    b = random.randint(1, 60)
    while a == b:  # 确保两个点不同
        b = random.randint(1, 60)
    
    # 计算均值和差值
    mean = int((a + b) / 2)  # 均值取整
    diff = abs(a - b)        # 差值
    
    # 统计均值和差值
    mean_counts[mean - 1] += 1
    diff_counts[diff] += 1

# 绘制均值统计图
plt.figure(figsize=(12, 6))

# 均值统计图
plt.subplot(1, 2, 1)
plt.bar(range(1, 61), mean_counts, color='blue')
plt.xlabel('均值 (1-60)')
plt.ylabel('出现次数')
plt.title('均值的出现次数')
plt.xticks(range(1, 61, 5))  # 设置X轴的刻度，每5个标记一个
plt.ylim(0, max(mean_counts) + 1000)  # 设置Y轴的范围，略大于最大次数

# 差值统计图
plt.subplot(1, 2, 2)
plt.bar(range(0, 60), diff_counts, color='green')
plt.xlabel('差值 (0-59)')
plt.ylabel('出现次数')
plt.title('差值的出现次数')
plt.xticks(range(0, 60, 5))  # 设置X轴的刻度，每5个标记一个
plt.ylim(0, max(diff_counts) + 1000)  # 设置Y轴的范围，略大于最大次数

plt.tight_layout()  # 调整子图间距
plt.show()
