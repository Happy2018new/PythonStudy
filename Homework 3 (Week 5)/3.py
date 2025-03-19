num = int(input("输入一个正整数:"))
ans = 0

i = 1
while i * i <= num:
    if num % i == 0:
        if i == num // i:
            ans += i
        else:
            ans += i + num // i
    i += 1

print("所有正因数的和为:" + str(ans))
