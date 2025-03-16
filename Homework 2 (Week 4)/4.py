a = float(input())
b = float(input())
c = float(input())

if a == 0:
    if b == 0:
        if c != 0:
            print("无解")
        else:
            print("x为任意实数")
    else:
        print("x=" + str(-c / b))
else:
    delta = b * 2 - 4 * a * c
    if delta >= 0:
        x1 = (-b - delta**0.5) / (2 * a)
        x2 = (-b + delta**0.5) / (2 * a)
        print("x1=" + str(x1))
        print("x2=" + str(x2))
    else:
        print("x无实数解")
