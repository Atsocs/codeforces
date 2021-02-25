def foo(x):
    a = 1
    while 2 * a ** 3 <= x:
        b3 = x - a ** 3
        b = round(b3 ** (1 / 3))
        if a ** 3 + b ** 3 == x:
            return True
        a += 1
    return False


def main():
    t = int(input())
    for case in range(t):
        x = int(input())
        print('YES' if foo(x) else 'NO')


if __name__ == "__main__":
    main()
