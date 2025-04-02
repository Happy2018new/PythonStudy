news_titles = []
while True:
    print("请输入新闻标题（输入空白字符停止）:")
    in_str = input()
    if in_str == "":
        break
    news_titles.append(in_str)

print("请输入查找的关键词:")
key_word = input()

count = 0
out = []
for i in news_titles:
    if key_word in i:
        count = count + 1
        out.append(i)

print("包括'{}'关键词的新闻共{}个".format(key_word, count))
print("筛选后的新闻列表为:")
for i in out:
    print(i)
