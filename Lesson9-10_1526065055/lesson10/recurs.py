def run(a,b):
    print("run {} - {}".format(a,b))
def go():
    print("rrr")
def eat():
    print("chav-cnaf")
a={}
a['run']=run
def error():
    print("Error")
if __name__ == '__main__':
    com = input("->")
    a.get(com,error)()
