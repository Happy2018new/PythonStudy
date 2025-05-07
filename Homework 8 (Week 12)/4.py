ORD_A = ord("a")

s = input()
s = s.lower()

ans = [0 for _ in range(25)]
for i in s:
    index = ord(i) - ORD_A
    if 0 <= index <= 25:
        ans[index] += 1

for index, value in enumerate(ans):
    if value == 0:
        continue
    print(f"{chr(ORD_A + index)}:{value}")
