ans = 0
for i in range(1, 967):
    if i % 2 == 0:
        ans -= i
    else:
        ans += i
print(ans)
