#2
def sum(inputfile, filename):
    with open(inputfile, 'r', encoding='utf-8') as f:
        b=[]
        for i in f.readlines():
            a = i.split()
            b.append(int(a[0]) + int(a[1]))
        with open(filename,'w',encoding='utf-8') as f2:
            for i in b:
                f2.write('\n%s'%str(i))









