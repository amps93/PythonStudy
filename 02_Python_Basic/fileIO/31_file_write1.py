#파일에 쓰기 : 파일을 쓰기 모드로 열고 파일객체의 write()함수를 이용하여 파일에 출력(기록)

data = 'hello, 안녕하세요'
f = open('file2.txt','w') #파일 객체
f.write(data)
f.close()

#한글이 깨져 보임
data = 'hello, 안녕하세요'
f = open('file2.txt','w', encoding='utf-8') #파일 객체
f.write(data)
f.close()