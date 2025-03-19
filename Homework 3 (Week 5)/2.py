def gcd(a: int, b: int) -> int:
    return gcd(b, a % b) if a % b != 0 else b


def lcm(a: int, b: int) -> int:
    return a * b // gcd(max(a, b), min(a, b))


a = int(input())
b = int(input())

print(lcm(a, b))
