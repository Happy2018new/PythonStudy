LEN_MAX = 7
STEP = 2

for i in range(1, LEN_MAX + STEP, STEP):
    space_len = (LEN_MAX - i) // 2
    print(" " * space_len, end="")
    print("*" * i, end="")
    print(" " * space_len)

for i in range(LEN_MAX - STEP, 1 - STEP, -STEP):
    space_len = (LEN_MAX - i) // 2
    print(" " * space_len, end="")
    print("*" * i, end="")
    print(" " * space_len)
