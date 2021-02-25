def acc(a):
    b = list(a[:])
    for i in range(1, len(a)):
        b[i] = b[i - 1] + a[i]
    return b


def special_indices(a):
    acc_v = acc(count(a))
    return [0] + acc_v[:-1]


def count(a):
    def rec(l, r):
        if r - l <= 0:
            return []
        if a[l] == a[r - 1]:
            return [r - l]

        m = (l + r) // 2
        ae = rec(l, m)
        ad = rec(m, r)
        if a[m - 1] != a[m]:
            return ae + ad
        return ae[:-1] + [ae[-1] + ad[0]] + ad[1:]

    return rec(0, len(a))


def f(a):
    si = special_indices(a)
    s = sum(a)
    n = len(a)
    _min = s - n * a[0]
    _i = 0
    for i in si:
        v = s - (n - i) * a[i]
        if v < _min:
            _min = v
            _i = i
    # print('i', _i)
    return _min


def foo(a):
    a.sort()
    a = count(a)
    a.sort()
    return f(a)


def main():
    t = int(input())
    for case in range(t):
        n = int(input())
        a = input()
        a = [int(i) for i in a.split()]
        print(foo(a))


if __name__ == "__main__":
    main()
