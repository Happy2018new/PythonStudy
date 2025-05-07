s = input()

out = ""
for i in s:
    if i not in out:
        out += i
print(out)
