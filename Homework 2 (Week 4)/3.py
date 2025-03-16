if bool(int(input("是否有票?有(1)/无(0):"))):
    if bool(int(input("是否携带刀具?有(1)/无(0):"))):
        print("请安检")
    else:
        print("请进站")
else:
    print("不能进站")
