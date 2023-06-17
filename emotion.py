from textblob import TextBlob
import csv

# 用于存储情感分析结果
sentiments = {
    '积极': 1,
    '消极': 0,
    '中性': 0
}

# 读取CSV文件
with open('武汉旅游.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        content = row[1]
        # 执行情感分析
        blob = TextBlob(content)
        sentiment = blob.sentiment.polarity
        # 更新情感计数
        if sentiment > 0:
            sentiments['积极'] += 1
        elif sentiment < 0:
            sentiments['消极'] += 1
        else:
            sentiments['中性'] += 1

# 输出频数
for sentiment, count in sentiments.items():
    print(sentiment + ':', count)
