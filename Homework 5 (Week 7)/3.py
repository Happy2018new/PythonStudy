numbers = []
while True:
    num_str = input()
    if num_str == "":
        break
    numbers.append(int(num_str))

print(max(numbers))
print(min(numbers))

numbers.sort(reverse=True)
sort_result = ""
for i in numbers:
    sort_result += str(i) + " "
print(sort_result)
