def acc(a):
    b = a[:]
    for i in range(1, len(a)):
        b[i] = b[i - 1] + a[i]
    return b


def can_win(a):
    def recursive(left, right):
        middle = left + (right - left) // 2
        if left > right:
            return middle
        b = [0] + acc(a)
        status = True
        for i in range(len(a)):
            if i == middle:
                continue
            extra = a[middle] if i <= middle else 0
            if extra + b[i] < a[i]:
                status = False
                break
        if status:
            return recursive(left, middle - 1)
        else:
            return recursive(middle + 1, right)

    m = recursive(0, len(a) - 1) + 1
    return [False for _ in range(m)] + [True for _ in range(len(a) - m)]


def foo(a):
    p, a = zip(*sorted(enumerate(a), key=lambda x: x[1]))
    a = list(a)
    can = can_win(a)
    can = sorted([p[i] + 1 for i in range(len(can)) if can[i]])
    print(len(can))
    print(' '.join([str(i) for i in can]))


def main():
    t = int(input())
    for case in range(t):
        n = int(input())
        a = input()
        a = [int(i) for i in a.split()]
        foo(a)


if __name__ == "__main__":
    main()
