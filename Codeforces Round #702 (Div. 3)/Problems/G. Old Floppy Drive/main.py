from math import ceil


def acc(a):
    b = a[:]
    for i in range(1, len(a)):
        b[i] = b[i - 1] + a[i]
    return b


# noinspection PyTypeChecker
def foo(a, x, n, m):
    s = sum(a)
    acc_a = acc(a)
    mb = max(acc_a)
    b = [None for _ in range(m)]
    r = [None for _ in range(m)]
    for j in range(m):
        total = x[j]
        if total <= mb:
            b[j] = 0
            r[j] = next(i for i in range(n) if total <= acc_a[i])
            continue
        if s <= 0:
            r[j] = -1
            continue
        b[j] = ceil((total - mb) / s)
        r[j] = next(n * b[j] + i for i in range(n)
                    if total <= acc_a[i] + b[j] * s)
        continue
    # print(r)
    print(b)
    return ' '.join(map(str, r))


def main():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        x = list(map(int, input().split()))
        print(foo(a, x, n, m))


if __name__ == "__main__":
    main()
