num = int(input("输入一个正整数:"))
ans = 0

i = 1
while i * i <= num:
    if num % i == 0:
        num_a, num_b = i, num // i
        if num_a == num_b:
            ans = ans + num_a
        else:
            ans = ans + num_a + num_b
    i += 1

print("所有正因数的和为:" + str(ans))
