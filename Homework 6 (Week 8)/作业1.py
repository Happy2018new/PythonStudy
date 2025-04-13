n = input()

a = {}
b = 0

for i in n:
    if not i in a:
        a[int(i)] = 1

for i in a:
    b = b + i

print(b)
