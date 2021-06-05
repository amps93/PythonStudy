#파일 생성 : 파일명만 적기
# f = open('file1.txt','w')
# f.close()
#생성된 file1.txt. 파일은 빈파일

##파일의 절대 경로
#경로 수정
# f = open('C:/Users/Amps/Desktop/Study/Multicampus/PythonStudy/fileIOfile1.txt','w')
# f.close()

#경로 수정 : 디렉토리가 존재하지 않는 경우
# f = open('C:/Users/Amps/Desktop/Study/Multicampus/Python/fileIOfile1.txt','w')
# f.close()

#경로 수정 : 디렉토리 경로 설정 시 오류 (\사용 => \\ 또는 / 사용해야됨)
# f = open('C:\\Users\\Amps\\Desktop\\Study\\Multicampus\\PythonStudy\\fileIOfile1.txt','w')
# f.close()

##파일의 상대경로
# f = open('./file1.txt','w') #현재 폴더
# f = open('../file1.txt','w') #현재 폴더의 상위 폴더
# f.close()