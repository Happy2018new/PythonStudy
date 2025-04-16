def get_prime_list(max_n: int) -> list[bool]:
    max_n += 1
    is_prime = [True for _ in range(max_n)]

    for i in range(min(2, max_n)):
        is_prime[i] = False

    for i in range(2, max_n):
        for j in range(2, i + 1):
            if i * j >= max_n:
                break
            is_prime[i * j] = False
            if i % j == 0:
                break

    return is_prime


def is_prime(n: int) -> bool:
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


# O(n)
hit_count = 0
prime_list = get_prime_list(999)
for i in range(2, 999 + 1):
    if prime_list[i]:
        hit_count += 1
print(hit_count)

# O(n*sqrt(n))
hit_count = 0
for i in range(2, 999 + 1):
    if is_prime(i):
        hit_count += 1
print(hit_count)
