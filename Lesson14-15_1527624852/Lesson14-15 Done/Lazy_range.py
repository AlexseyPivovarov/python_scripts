def l_range(start, stop=None, step=0.1):
    if stop is None:
        start, stop = 0.0, start
    try:
        start = float(start)
        stop = float(stop)
        step = float(step)
    except ValueError:
        raise TypeError("object cannot be interpreted as an float")
    except TypeError:
        raise TypeError("object cannot be interpreted as an float")
    i = 1
    a = start
    while a < stop if step >= 0 else a > stop:
        yield a
        a = start + step * i
        i += 1
    yield a


if __name__ == '__main__':
    gen = l_range(1.9, 0.1, -0.2)
    for item in gen:
        print(item)
    print("-----------------------------")
    gen = l_range(0.1, 1.9, 0.2)
    for item in gen:
        print(item)
    print("-----------------------------")
    gen = l_range(1.9)
    for item in gen:
        print(item)




