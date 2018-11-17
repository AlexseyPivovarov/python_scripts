gen=(i for i in  range(10))
while True:
    try:
        print(next(gen))
    except StopIteration:
        break
