"""
Accomplished using the EduTools plugin by JetBrains https://plugins.jetbrains.com/plugin/10081-edutools
"""
from math import log2, ceil


def foo(arr):
    n = len(arr)
    acc = 0
    for i in range(n - 1):
        a = min(arr[i], arr[i + 1])
        b = max(arr[i], arr[i + 1])
        if a != b:
            acc += (ceil(log2(b / a)) - 1)
    return acc


if __name__ == "__main__":
    # Write your solution here
    t = int(input())
    for case in range(t):
        n = int(input())
        a = []
        x = input()
        x = [int(i) for i in x.split()]
        print(foo(x))
