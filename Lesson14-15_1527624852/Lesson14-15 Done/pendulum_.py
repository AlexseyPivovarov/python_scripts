def pendulum(n, m, s):
    while True:
        for i in range(n, m, s):
            yield i
        for i in range(m, n, -s):
            yield i


if __name__ == '__main__':
    a = pendulum(1, 10, 2)
    for _ in range(20):
        print(next(a))
