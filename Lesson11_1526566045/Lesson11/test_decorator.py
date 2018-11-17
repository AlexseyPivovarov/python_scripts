import time
def test_f_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        a = func(*args, **kwargs)
        end = time.time()
        name = func.__name__
        print("Func {} time={}".format(name,round(end-start,6)))
        return a
    return wrapper
