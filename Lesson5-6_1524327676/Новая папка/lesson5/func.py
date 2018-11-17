def test(name):
    print("Hello, {}!".format(name))
name = "Voba"
test(name)
high=1000
def test_func(a,b):
    try:
        return a/b
    except:
        return 0

a = test_func(20,10)
print(a)
