users: dict[str, str] = {
    "张三": "123456",
    "李四": "abcdef",
    "王五": "123abc",
    "刘六": "aaa111",
}

print("所有用户的姓名: ")
for i in users.keys():
    print(i, end=" ")
print()

print("张三密码:", users.get("张三"))
