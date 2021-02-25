"""
Accomplished using the EduTools plugin by JetBrains https://plugins.jetbrains.com/plugin/10081-edutools
"""


def solve(a):
    ones, twos = map(a.count, [1, 2])
    s = ones + 2 * twos
    is_odd = s % 2 == 1
    if is_odd:
        return False
    target = s // 2
    for i in range(ones + 1):
        for j in range(twos + 1):
            if i + 2 * j == target:
                return True
    return False


def main():
    for case in range(int(input())):
        input()
        a = tuple(map(int, input().split()))
        print('YES' if solve(a) else 'NO')


if __name__ == "__main__":
    main()
