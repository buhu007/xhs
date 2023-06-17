import jieba
from collections import Counter
from pyecharts.charts import WordCloud
from pyecharts.globals import SymbolType
import re
import json
import emoji

jieba.load_userdict('C:/Users/Administrator/Desktop/wuhanlvy/app01/static/custom_dict.txt')

# 假设您的评论数据存储在一个名为comments的list中

def cy(comments):
    # 定义停用词和正则表达式
    stopwords = ["的","去","吃", "很", "有点", "是", "就", "了", "还", "都", "也", "和","元"
                  , "不错", "太", "不", "非常", "好", "很好", "可以", "这个", "有"]
    pattern = re.compile("[^\u4e00-\u9fa5]+")

    # 去除HTML标签和特殊字符
    comments = [re.sub('<[^<]+?>', '', comment) for comment in comments]
    comments = [re.sub(pattern, '', comment) for comment in comments]

    # 分词并去掉停用词
    words = []
    for comment in comments:
        words += [word for word in jieba.cut(comment) if word not in stopwords]

    # 统计词频
    word_count = Counter(words)

    # 删除非汉字的符号、标点、表情符号
    top_words = {re.sub('[^\u4e00-\u9fa5]+', '', word): count for word, count in word_count.items() if re.sub('[^\u4e00-\u9fa5]+', '', word)}

    # 按频数降序排序并取前200个关键词
    top_words = dict(sorted(top_words.items(), key=lambda x: x[1], reverse=True)[:200])

    # 将Python字典转换为JSON格式数据
    json_data = json.dumps(top_words, ensure_ascii=False)

    # 生成词云图
    wordcloud = WordCloud()
    wordcloud.add("", list(top_words.items()), word_size_range=[20, 100], shape=SymbolType.DIAMOND)
    wordcloud.set_global_opts(title_opts={"text": "评论关键词词云图", "subtext": "前200个关键词"})
    wordcloud.render("m1.html")

    return top_words
