f= open('test2.txt','r',encoding='utf-8')
lines = f.readlines()
print(lines)
f.close()

#readlines()로 읽은 내용을 한 줄씩 출력하기
f= open('test2.txt','r',encoding='utf-8')
lines = f.readlines()
for i in lines:
    print(i,end='')
f.close()