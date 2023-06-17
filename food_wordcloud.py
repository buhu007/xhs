import csv
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba
from collections import Counter
import numpy as np

from matplotlib import font_manager

# 设置字体路径
font_path = r'C:\Users\Administrator\Desktop\wuhanlvy\app01\utils\SimHei.ttf'  # 替换为实际的字体文件路径

# 加载字体
font_manager.fontManager.addfont(font_path)

# 设置字体
plt.rcParams['font.family'] = 'SimHei'  # 将 'SimHei' 替换为您选择的字体名称

# 加载自定义词典
jieba.load_userdict('words.txt')

# CSV 文件路径
csv_path = r'C:\Users\Administrator\Desktop\wuhanlvy\武汉美食.csv'
# 替换为内容列的列名
content_column = '内容'

words = []
with open(csv_path, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        content = row[content_column]
        words.extend(jieba.lcut(content))

filtered_words = [word for word in words if
                  word in ["宽粉", "石头饼", "烧麦", "毛肚", "虾滑", "条头糕", "热干面", "豆皮", "生煎", "鱼", "藕",
                           "面窝", "小龙虾", "周黑鸭", "武昌鱼", "牛肉粉", "砂锅", "烧烤", "冰粉", "蛋烘糕", "火锅",
                           "油条", "包子", "炸鸡", "馅饼", "片皮鸭"]]

word_count = Counter(filtered_words)

# 按降序对词频统计结果进行排序
sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

# 取出排序后的词汇和词频
labels = [word for word, count in sorted_word_count[:12]]
sizes = [count for word, count in sorted_word_count[:12]]

# 生成饼状图
plt.figure(figsize=(8, 6))
patches, _ = plt.pie(sizes, startangle=90, wedgeprops={'edgecolor': 'white'})
plt.axis('equal')  # 保证饼状图是正圆形

# 添加美食名称标注
for i, patch in enumerate(patches):
    angle = (patch.theta2 - patch.theta1) / 2.0 + patch.theta1
    x = patch.r * 0.5 * np.cos(np.radians(angle))
    y = patch.r * 0.5 * np.sin(np.radians(angle))
    bbox_props = dict(facecolor='white', edgecolor='black', boxstyle='square')

    if i < 12:
        plt.text(x, y, labels[i], ha='center', va='center', bbox=bbox_props)

# 添加大标题
plt.title('武汉美食热度饼状图')

plt.show()
