#파일 내에서 검색
#seek(offset, whence) 함수

print('-----파일 내에서 검색 seek()-----')
f = open('test3.txt','r',encoding='utf-8')
f.seek(0,0) #시작위치 0행 0열
f.seek(1,0) #시작위치 0행 7열
f.seek(7,0) #시작위치 1행 0열
f.seek(14,0)
lines = f.readlines()
print(lines)
f.close()

