ma_qiang_company_products: list[list] = [
    ["iphone", 1200],
    ["xiaomi", 2000],
    ["huawei", 4500],
    ["vivo", 1800],
]

xiao_mi_company_products: list[list] = [
    ["xiaomi", 1800],
    ["vivo", 1500],
    ["honor", 2300],
    ["oppo", 2200],
]

merge_ans: dict[str, int] = {}
for i in ma_qiang_company_products + xiao_mi_company_products:
    phone_brand: str = i[0]
    phone_cut: int = i[1]
    if phone_brand in merge_ans:
        merge_ans[phone_brand] += phone_cut
    else:
        merge_ans[phone_brand] = phone_cut


print("合并后商品清单如下所示。")
for key, value in merge_ans.items():
    print("商品名: {} | 商品数量: {}".format(key, value))
