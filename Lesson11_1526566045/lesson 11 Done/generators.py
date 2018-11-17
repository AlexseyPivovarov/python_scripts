[print("{: ^5}".format("*" * i)) for i in [1, 3, 5, 3, 1]]
print("--------")
[print("{:8^5}".format(" " * i)) for i in [3, 1, 0]]
print("--------")
[print("1" * i) for i in range(1, 6)]
print("--------")
[print("{}{}".format(i % 2, (i + 1) % 2) * 4) for i in range(4)]
print("--------")
[print("{}{}".format(i, j) * 4) for i, j in zip([0, 1, 0, 1], [1, 0, 1, 0])]
