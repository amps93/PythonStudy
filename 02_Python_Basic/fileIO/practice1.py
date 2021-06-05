#1
with open('yesterday.txt','r') as f:
    lylics = f.read()
    lylics = lylics.lower()
    a = lylics.split()
    count = {}
    for i in a:
        try :
            count[i] += 1
        except :
            count[i] = 1
    for i,j in count.items():
        print(i, ': %d'%j)
    count = {}
    # for i in range(len(a)):
    #     if a[i] in count:
    #         count[a[i]] += 1
    #     else:
    #         count[a[i]] = 1
    # print(count)








