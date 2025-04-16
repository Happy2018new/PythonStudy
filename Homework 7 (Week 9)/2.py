def get_line(char: str, line_id: int, last_line_id: int) -> str:
    occupy_count = 2 * line_id - 1
    last_line_char_count = 2 * last_line_id - 1

    delta = last_line_char_count - occupy_count
    half_empty = delta // 2

    return " " * half_empty + char * occupy_count + " " * half_empty


for i in range(1, 6 + 1):
    print(get_line("*", i, 6))
