s = input()
s = s.strip()

string_list = s.split(" ")
string_list = [i[0].upper() + i[1:].lower() for i in string_list]

if len(string_list) <= 2:
    print(" ".join(string_list))
    exit()

newer_one = [string_list[0]]
for i in range(1, len(string_list)):
    single_str = string_list[i]
    if i == len(string_list) - 1:
        newer_one.append(single_str)
    else:
        newer_one.append(f"{single_str[0]}.")
print(" ".join(newer_one))
