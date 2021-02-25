"""
Accomplished using the EduTools plugin by JetBrains https://plugins.jetbrains.com/plugin/10081-edutools
"""


def foo(x):
    c = [0, 0, 0]
    for i in range(len(x)):
        c[x[i] % 3] += 1
    steps = 0
    goal = int(len(x) / 3)
    for m in range(3):
        for i in range(3):
            j = (i + 1) % 3
            if c[i] > goal:
                passou = c[i] - goal
                c[i] -= passou
                c[j] += passou
                steps += passou
    return steps


if __name__ == "__main__":
    # Write your solution here
    t = int(input())
    for case in range(t):
        n = int(input())
        x = input()
        x = [int(i) for i in x.split()]
        print(foo(x))
