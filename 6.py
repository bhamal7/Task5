f = open("doc.txt","r")
for i in f.readlines():
    for j in i.split(' '):
        if (len(j) % 2 == 0):
            print(j)

f.close()