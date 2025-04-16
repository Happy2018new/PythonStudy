def get_max_one(data: list[tuple[str, str, int]]) -> tuple[str, str, int]:
    max_one: tuple[str, str, int] = data[0]
    for i in data:
        if i[2] > max_one[2]:
            max_one = i
    return max_one


table_origin = """
序号	标题	分类	阅读量
1	科技发展新动态	科技	1500
2	股市最新消息	财经	2200
3	最新科技产品评测	科技	1800
4	国际油价波动	财经	400
5	体育赛事报道	体育	1400
6	网络安全新威胁	科技	800
7	金融市场分析	财经	2250
8	艺术展览开幕	文化	900
9	环保政策解读	环保	500
10	健康生活小贴士	健康	450

"""

fixed_table: list[tuple[str, str, int]] = []
for i in table_origin.split("\n"):
    split_result = i.split()

    if len(split_result) != 4:
        continue
    if split_result[3] == "阅读量":
        continue

    fixed_table.append(
        (split_result[1], split_result[2], int(split_result[3])),
    )

max_one = get_max_one(fixed_table)
print("新闻阅读量最大的新闻信息如下: ")
print(f"新闻标题: {max_one[0]} | 新闻分类: {max_one[1]} | 新闻阅读量: {max_one[2]}")
