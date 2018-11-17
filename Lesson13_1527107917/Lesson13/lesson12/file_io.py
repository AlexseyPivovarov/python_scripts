#-*-utf-8-*-
a = open('test',"wb")
i  = "#".join((str(i) for i in range(100)))
a.write(i.encode())
with open('test', "wb") as f:
    f.write("12345".encode())
