import threading
arg=1000
ts = []
def f(id):
    global arg
    while arg:
        with open('thread.txt', 'a') as fs:
            fs.write('thread ={} arg={}\n'.format(id,arg))
        arg-=1
        if arg<0:
            break
def main():
    for i in range(10):
        t = threading.Thread(target=f, args=(i,))
        t.start()
        ts.append(t)
    for t in ts:
        print(t.name)
        t.join()
if __name__ == '__main__':
    main()
