katok = ['다현', '정현', '쯔위', '사나', '지효']

def insert_data(position, friend):
    katok.append(None)
    klen = len(katok)

    for i in range(klen-1, position, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None

    katok[position] = friend

insert_data(2, '설라')
print(katok)