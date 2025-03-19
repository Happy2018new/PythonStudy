n = int(input())

if n % 2 != 0:
    print((1 + n) * ((n - 1) // 2 + 1) // 2)
else:
    print(n * ((n - 2) // 2 + 1) // 2)
