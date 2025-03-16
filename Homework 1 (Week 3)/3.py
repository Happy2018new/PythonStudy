num = int(input())

a = num // 100
b = (num - a * 100) // 10
c = num - a * 100 - b * 10

print(a * a * a + b * b * b + c * c * c)
