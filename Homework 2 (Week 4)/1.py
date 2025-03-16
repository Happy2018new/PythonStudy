year = int(input("输入年份:"))
month = int(input("输入月份:"))

if month == 1:
    print(str(year) + "年" + str(month) + "月有31天")
if month == 3:
    print(str(year) + "年" + str(month) + "月有31天")
if month == 4:
    print(str(year) + "年" + str(month) + "月有30天")
if month == 5:
    print(str(year) + "年" + str(month) + "月有31天")
if month == 6:
    print(str(year) + "年" + str(month) + "月有30天")
if month == 7 or month == 8:
    print(str(year) + "年" + str(month) + "月有31天")
if month == 9:
    print(str(year) + "年" + str(month) + "月有30天")
if month == 10:
    print(str(year) + "年" + str(month) + "月有31天")
if month == 11:
    print(str(year) + "年" + str(month) + "月有30天")
if month == 12:
    print(str(year) + "年" + str(month) + "月有31天")

if month == 2:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(str(year) + "年" + str(month) + "月有29天")
    else:
        print(str(year) + "年" + str(month) + "月有28天")
