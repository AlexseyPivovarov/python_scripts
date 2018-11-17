PI = 3.1415796
print("Hello!")

def squire(r):
    if r==0:
        print("file name for func",__name__)
        print("PI= in func",PI)
    return 2*PI
def hello():
    print("hellooooooooooo!!!!!!")

if __name__ == '__main__':
    print("PI after func",PI)
    print("file name",__name__)
    print("PI=",PI)
    print(squire(3))
