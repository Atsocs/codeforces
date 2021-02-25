
from math import ceil


def acc(a):
    b = a[:]
    for i in range(1, len(a)):
        b[i] = b[i - 1] + a[i]
    return b


def query(a, n, total):
    s = sum(a)
    b = acc(a)
    _min = min(b)
    _max = max(b)
    if s <= 0:
        if total > _max:
            return -1
        else:  # total <= max
            return next(i for i in range(n) if total <= b[i])
    else:  # s > 0
        if total <= _max:
            return next(i for i in range(n) if total <= b[i])
        else:  # total > max
            blocks = ceil((total - _max) / s)
            return next(n * blocks + i for i in range(n) if total <= b[i] + blocks * s)


def foo(a, x, n, m):
    results = []
    for j in range(m):
        results.append(query(a, n, x[j]))
    return ' '.join(map(str, results))


def main():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        x = list(map(int, input().split()))
        print(foo(a, x, n, m))


if __name__ == "__main__":
    main()
