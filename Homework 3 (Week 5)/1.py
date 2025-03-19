n = int(input())

if n % 2 != 0:
    print((1 + n) * ((n - 1) // 2 + 1) // 2)
else:
    n -= 1
    print((1 + n) * ((n - 1) // 2 + 1) // 2)
