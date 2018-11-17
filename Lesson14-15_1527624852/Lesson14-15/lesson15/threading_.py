import threading
import time
arg=10
def f(id):
    global arg
    while arg:
        print('thread ={} arg={}'.format(id,arg))
        arg-=1
        if arg<0:
            break
for i in range(5):
    t = threading.Thread(target=f, args=(i,))
    t.start()
