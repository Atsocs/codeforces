from math import ceil


def acc(a):
    b = a[:]
    for i in range(1, len(a)):
        b[i] = b[i - 1] + a[i]
    return b


# noinspection PyTypeChecker
def foo(a, x, n, m):
    s = sum(a)
    b = acc(a)
    mb = max(b)
    results = [None for _ in range(m)]
    for j in range(m):
        if results[j] is not None:
            continue
        xj = x[j]
        if xj <= mb:
            results[j] = next(i for i in range(n) if xj <= b[i])
    # total > m
    if s <= 0:
        for j in range(m):
            if results[j] is not None:
                continue
            results[j] = -1
    # s > 0
    for j in range(m):
        if results[j] is not None:
            continue
        xj = x[j]
        blocks = ceil((xj - mb) / s)
        results[j] = next(n * blocks + i for i in range(n)
                          if xj <= b[i] + blocks * s)
    assert all([x is not None for x in results])
    return ' '.join(map(str, results))


def main():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        x = list(map(int, input().split()))
        print(foo(a, x, n, m))


if __name__ == "__main__":
    main()
