from main import foo

N = 20000
N = N // 2
a = sum([[2 * n, -2 * n] for n in range(1, N)], start=[1]) + [2 * N]
NN = 2 * N + 1
x = [i * NN for i in range(1, 11)]
n, m = len(a), len(x)
# print(" ".join(map(str, a)))
print(foo(a, x, n, m))
