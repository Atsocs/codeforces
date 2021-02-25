"""
Accomplished using the EduTools plugin by JetBrains https://plugins.jetbrains.com/plugin/10081-edutools
"""


def trailing_zeroes(x):
    x = "{0:b}".format(int(x))
    return len(x) - len(x.rstrip('0'))


def solve(w, h, n):
    tw, th = list(map(trailing_zeroes, [w, h]))
    pieces = 2 ** (tw + th)
    return n <= pieces


def main():
    for case in range(int(input())):
        w, h, n = tuple(map(int, input().split()))
        print('YES' if solve(w, h, n) else 'NO')


if __name__ == "__main__":
    main()
