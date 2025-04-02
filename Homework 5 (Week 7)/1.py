scores = []
for _ in range(5):
    scores.append(int(input()))

out = []
for i in scores:
    if 90 <= i <= 100:
        out.append("A")
    if 80 <= i < 90:
        out.append("B")
    if 70 <= i < 80:
        out.append("C")
    if 60 <= i < 70:
        out.append("D")
    if 0 <= i < 60:
        out.append("E")

print(scores)
print(out)
