n = int(input())

data = []
for _ in range(n):
    data.append(int(input()))

out = []

for i in data:
    if not i in out:
        out.append(i)

print(data)
print(out)
