origin_data: list[dict[str, str]] = [
    {"标题": "科技发展新动态", "分类": "科技"},
    {"标题": "股市最新消息", "分类": "财经"},
    {"标题": "最新科技产品评测", "分类": "科技"},
    {"标题": "国际油价波动", "分类": "财经"},
    {"标题": "体育赛事报道", "分类": "体育"},
    {"标题": "网络安全新威胁", "分类": "科技"},
    {"标题": "金融市场分析", "分类": "财经"},
    {"标题": "艺术展览开幕", "分类": "文化"},
    {"标题": "环保政策解读", "分类": "环保"},
    {"标题": "健康生活小贴士", "分类": "健康"},
]

ans: dict[str, int] = {}
for i in origin_data:
    news_type = i.get("分类")
    if news_type in ans:
        ans[news_type] += 1
    else:
        ans[news_type] = 1

sorted_ans = ans.items()
sorted(sorted_ans, key=lambda x: x[1], reverse=True)

for key, value in sorted_ans:
    print("新闻类别为 {} 的数量为 {}".format(key, value))
