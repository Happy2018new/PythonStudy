s = input()
s = s.strip()

string_list = s.split(" ")
string_list = [i[0].upper() + i[1:].lower() for i in string_list]

print(" ".join(string_list))
