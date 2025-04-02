# 你不应该使用该代码提交作业，
# 因为它使用了 **算法** 知识。
#
# 用到的知识点如下：
#       - 二分
#       - 排序
#
# 本代码对 2.py 中原有的实现进行了优化，
# 将原本最坏情况下 ~O(n**2) 的时间复杂度
# 降低到了最坏情况下 ~O(n*log(n))


def upper_bound(list_in: list, try_num: int) -> int:
    """
    Search the first element x from list_in
    that satisfied x=list_in[i][0] > try_num.

    Args:
        list_in (list[tuple[int, int]]): The given list
        try_num (int): The given number that want to satisfy

    Returns:
        int: The index of the first element that bigger than try_num.
             Return -1 for not exist.
    """
    l = 0
    r = len(list_in) - 1
    result = -1

    while l <= r:
        mid = (l + r) // 2
        if list_in[mid][0] > try_num:
            result = mid
            r = mid - 1
        else:
            l = mid + 1

    return result


n = int(input())

data = []
for i in range(n):
    data.append((int(input()), i))
out_1 = [i[0] for i in data]
data = sorted(data)


result = []
ptr = 0
while True:
    result.append(data[ptr])
    ptr = upper_bound(data, data[ptr][0])
    if ptr == -1:
        break

result = sorted(result, key=lambda x: x[1])


out_2 = [i[0] for i in result]
print(out_1)
print(out_2)
