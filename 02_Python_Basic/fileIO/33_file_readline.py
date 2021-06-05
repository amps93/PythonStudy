# #파일 읽어오기
# #readline() : 1개의 행씩 읽어오기, 행 끝에 \n이 포함
# #readlines() : 모든 행을 읽어 라인 단위로 잘라서 리스트를 생성
# #              ['...\n','...\n','...\n',...,'...\n']
# #read() : 내용 전체를 한 문자열로 반환
# print('----------첫번째 행 읽어오기-------------')
# f = open('test.txt','r')
# line = f.readline()
# print(line)
# f.close()
#
# #utf-8로 저장된 파일 읽기
# # f = open('test2.txt','r')
# # line = f.readline()
# # print(line)
# # f.close()
# #오류 발생
# #UnicodeDecodeError: 'cp949' codec can't decode byte 0xec in position 0: illegal multibyte sequence
# f = open('test2.txt','r',encoding='utf-8')
# line = f.readline()
# print(line)
# f.close()

#여러 줄 읽기
f = open('test2.txt','r',encoding='utf-8')
line = f.readline()
while True:
    line = f.readline()
    if line == '':
        break
    print(line,end='')
f.close()