#여러 줄의 데이터를 쓰기

f = open('file3.txt','w',encoding='utf-8')

for i in range(1,11):
    data = '%d행\n'%i
    f.write(data)
f.close()

#csv파일로 저장
f = open('file4.csv','w')
for i in range(1, 11):
    data = '%d행\n' % i
    f.write(data)
f.close()
