def merge_dict(src: dict[str, int], dst: dict[str, int]):
    for i in src:
        if not i in dst:
            dst[i] = src[i]
        else:
            dst[i] += src[i]


maqiang: dict[str, int] = {
    "iphone": 1200,
    "xiaomi": 2000,
    "huawei": 4500,
    "vivo": 1800,
}

liuyun: dict[str, int] = {
    "xiaomi": 1800,
    "vivo": 1500,
    "honor": 2300,
    "oppo": 2200,
}


merge_dict(maqiang, liuyun)

print("合并结果如下: ")
for key, value in liuyun.items():
    print(f"商品名: {key} | 商品数量: {value}")
