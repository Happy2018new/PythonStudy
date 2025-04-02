numbers = []
while True:
    num_str = input()
    if num_str == "":
        break
    numbers.append(int(num_str))

print(max(numbers))
print(min(numbers))

sort_result = sorted(numbers, reverse=True)
sort_result_out = ""
for i in sort_result:
    sort_result_out += str(i) + " "
print(sort_result_out)
