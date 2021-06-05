#append mode를 사용하여 파일 끝에 추가

f = open('test3.txt','a',encoding='utf-8')
data = '\n\n Python Programming'
f.write(data)

f.close()

#읽기모드로 파일을 열어서 내용 출력
f = open('test3.txt','a',encoding='utf-8')
data = 'R programming\n'
f.write(data)

f=open('test3.txt','r',encoding='utf-8')
print(f.read())

f.close()