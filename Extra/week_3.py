# 定义一些常量，用于评价一个练习生。
IDOL_PERFECT = 0  # 这个练习生很棒
IDOL_GOOD = 1  # 这个练习生良好
IDOL_MIDDLE = 2  # 这个练习生中等
IDOL_LOW = 3  # 这个练习生偏差
IDOL_BAD = 4  # 这个练习生很差

# 练习生基本信息
idol_name: list[str] = []  # 练习生的姓名
idol_unique_id: list[int] = []  # 练习生的编号
idol_height: list[float] = []  # 练习生的身高
idol_is_under_first_training: list[bool] = []  # 是否是首发练习生

# 练习生评估信息
idol_assess_total_count: list[int] = []  # 总评级次数
idol_assess_pass_count: list[int] = []  # 评级合格次数

# 读入每个练习生的信息。
# index 指示目前正在读取第 index 个练习生的信息。
index: int = 0
while True:
    # 上一个练习生的信息已完成读入，
    # 所以我们通过使 index 递增从而
    # 得到目前正在读入第几个练习生。
    index = index + 1
    # 依次读入这个练习生的各个信息
    name: str = input("输入第 " + str(index) + " 个练习生的名字: ")
    unique_id: int = int(input("输入这个练习生的编号: "))
    height: float = float(input("输入这个练习生的身高 (单位为厘米): "))

    is_under_first_training: bool = False
    temp: str = input("这个练习生是否是首发练习生 (回答 Yes 或 No): ")
    if temp == "Yes":
        is_under_first_training = True
    if temp != "Yes" and temp != "No":
        print("[错误] 未得到正确回答，此处认为该练习生不是首发练习生!")

    assess_total_count: int = int(input("输入这个练习生的市场评级次数: "))
    assess_pass_count: int = int(input("输入这个练习生的评级合格次数: "))
    # 将读入的值放入列表
    idol_name.append(name)
    idol_unique_id.append(unique_id)
    idol_height.append(height)
    idol_is_under_first_training.append(is_under_first_training)
    idol_assess_total_count.append(assess_total_count)
    idol_assess_pass_count.append(assess_pass_count)
    # 是否应该结束
    temp: str = input("是否还有其他练习生的数据等待录入? (回答 Yes 或 No): ")
    if temp == "No":
        print()
        break
    if temp == "Yes":
        print()
    if temp != "Yes" and temp != "No":
        print("[错误] 未得到正确回答，此处认为已经没有更多练习生!")
        print()
        break

# 排序处理。
# 因为我希望能按照练习生的编号从小到大进行处理
sort_prepare: list[tuple[int, int]] = [(idol_unique_id[i], i) for i in range(index)]
sort_prepare.sort()

# 依次处理每个练习生，
# 计算它们的市场合格率，
# 然后输出他们的信息
for i in sort_prepare:
    index: int = i[1]

    name: str = idol_name[index]
    unique_id: int = i[0]
    height: float = idol_height[index]
    is_under_first_training: bool = idol_is_under_first_training[index]
    assess_total_count: int = idol_assess_total_count[index]
    assess_pass_count: int = idol_assess_pass_count[index]

    pass_rate: float = 0
    if assess_total_count != 0:
        pass_rate: float = (assess_pass_count / assess_total_count) * 100
    pass_rate_code: int = IDOL_BAD

    if pass_rate >= 20:
        pass_rate_code = IDOL_LOW
    if pass_rate >= 40:
        pass_rate_code = IDOL_MIDDLE
    if pass_rate >= 60:
        pass_rate_code = IDOL_GOOD
    if pass_rate >= 80:
        pass_rate_code = IDOL_PERFECT

    print("编号为", unique_id, "的练习生的信息和评价如下: ")

    print("     - 练习生基本信息 -")
    print("         姓名:", name)
    print("         编号:", unique_id)
    print("         身高:", round(height, 2), "cm")
    if is_under_first_training:
        print("         是否是首发练习生: 是")
    else:
        print("         是否是首发练习生: 否")

    print("     - 练习生评级信息 -")
    print("         市场评级次数:", assess_total_count)
    print("         评级合格次数:", assess_pass_count)

    print("     - 系统评价 -")
    if assess_total_count != 0:
        print("         该练习生市场合格率:", str(round(pass_rate, 2)) + "%")
        if pass_rate_code == IDOL_PERFECT:
            print("         系统评语: 该练习生表现非常好")
        if pass_rate_code == IDOL_GOOD:
            print("         系统评语: 该练习生表现良好")
        if pass_rate_code == IDOL_MIDDLE:
            print("         系统评语: 该练习生表现中等")
        if pass_rate_code == IDOL_LOW:
            print("         系统评语: 该练习生表现偏差")
        if pass_rate_code == IDOL_BAD:
            print("         系统评语: 该练习生表现非常差")
    else:
        print("         评价不了一点，因为这个练习生没有参与过评级!")

# 输出结束语
print()
print("已处理所有练习生的数据，祝您生活愉快!")
