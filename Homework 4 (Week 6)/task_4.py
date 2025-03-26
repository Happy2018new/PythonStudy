cnt = 0
for i in range(500, 2026):
    if i % 7 == 0 and i % 10 == 2:
        cnt += 1
print(cnt)
