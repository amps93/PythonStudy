crawling = 'Data crawling is fun'

token = crawling.split()
print(token)

names = 'lee,kim,choi,kang'
print(names.split(','))

nameL = names.split(',')
for i in nameL:
    print(i)

for i in range(len(nameL)):
    print(nameL[i])

#문자열 하나씩 출력
# for i in crawling:
#     print(i)