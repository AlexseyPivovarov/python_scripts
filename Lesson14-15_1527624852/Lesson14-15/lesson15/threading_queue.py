import urllib.request
import threading
import queue

q = queue.Queue()
def geturl():
    while True:
        url, id=q.get()
        t=urllib.request.urlopen(url)
        print(len(t.read()),id)
        q.task_done()


for i in range(4):
    t=threading.Thread(target=geturl)
    t.daemon=True
    print(t.name)
    t.start()

for i in range(20):
    print("task{}".format(i))
    q.put(('https://ga.ua',i))

q.join()
