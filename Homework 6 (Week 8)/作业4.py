a=[]
#第一个老板
a.append(("iphone",1200))
a.append(("xiaomi",2000))
a.append(("huawei",4500))
a.append(("vivo",1800))
#第二个老板
a.append(("xiaomi",1800))
a.append(("vivo",1500))
a.append(("honor",2300))
a.append(("oppo",2200))
b={}
for i in a:
    if i[0] in b:
        b[i[0]] = b[i[0]] + i[1]
    else:
        b[i[0]] = i[1]

print("合并结果:")
for i in b:
    print("商品名:"+str(i)+"商品数量:"+str(b[i]))
