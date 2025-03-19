a = int(input())
b = int(input())

a1 = max(a, b)
b1 = min(a, b)

while a1 % b1 != 0:
    a1, b1 = b1, a1 % b1

print(a * b // b1)
