def f(b):
    print(__name__)
    b.append(34)


if __name__ == '__main__':
    b=[]
    f()
    print(b)
