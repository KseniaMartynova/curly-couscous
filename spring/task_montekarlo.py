import random
def f(x):
    return x ** 2 + 2 * x + 1
def integral(f, a, b, n):
    count = 0
    for i in range(n):
        x = random.uniform(a, b)
        y = random.uniform(0, f(b))
        if y <= f(x):
            count += 1
    return (count / n) * (b - a) * f(b)
a = -1
b = 1
n = 1000000
result = integral(f, a, b, n)
print(result)
