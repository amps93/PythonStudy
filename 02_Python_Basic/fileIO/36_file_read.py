# read() : 파일 전체를 읽어서 문자열 반환

f= open('test3.txt','r',encoding='utf-8')
data = f.read()
print(data)
print(type(data))
print(len(data))

for i in data:
    print(i)

f.close()