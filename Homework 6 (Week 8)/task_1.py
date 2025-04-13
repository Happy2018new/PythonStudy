n = input()

recoder: list[bool] = [False for _ in range(10)]
for i in n:
    recoder[int(i)] = True

ans = 0
for i in range(10):
    if recoder[i]:
        ans += i
print(ans)
