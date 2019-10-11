# coding=utf-8
# !@Author : YaoLei
import jieba
from wordcloud import WordCloud

file = '三国演义.测试文本'
fo = open(file, 'r', encoding='UTF-8')
t = fo.read()
fo.close()
# ls = jieba.cut(t, cut_all=True)
ls = jieba.lcut(t)
txt = ''.join(ls)
w = WordCloud(font_path='Deng.ttf', width=1200, height=800, background_color='white', max_words=200)
w.generate(txt)
w.to_file("三国演义.png")
