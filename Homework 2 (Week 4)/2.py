money_get = int(input("输入货款总价(元):"))
money_output = float(money_get)

if money_get > 1000:
    money_output = money_output * (1 - 0.15)
if 500 < money_get <= 1000:
    money_output = money_output * (1 - 0.10)
if 200 < money_get <= 500:
    money_output = money_output * (1 - 0.05)

print("支付款(元):" + str(money_output))
