def delete(command):
    print(command)
    del(command)
command = {
    "run":lambda item: "run"*int(item),
    "delete":delete
}

while True:
    com,value = input("go user->").split()
    command[com](value)
