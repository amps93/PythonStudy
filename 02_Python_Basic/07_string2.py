#string 관련 함수

#len():문자열의 length
print('-'*25,'len','-'*25)
string = "Python Programming"
print(len(string))

#count
print('-'*25,'count','-'*25)
print(string.count('m')) #문자열에서 m의 개수
print(string.count('o'))
print(string.count('p'))
print(string.count('ing'))

#find
print('-'*25,'find','-'*25)
print(string.find('ing'))
print(string.find('P'))
print(string.find('z')) #없으면 -1 return

#index
print('-'*25,'index','-'*25)
print(string.index('ing'))
print(string.index('P'))
#print(string.index('z')) #없으면 오류

#email type 체크
email = input('input email : ')
if(email.find('@')== -1 or
    email.find('.')==-1 or
    email.index('@')>email.index('.') or
    email.index('.') - email.index('@') < 0 or
    email.index('@') == 0 or
    len(email) - email.index('.') <= 1 or
    email.count('@') >= 2 or
    email.count('.') >= 2
    ):
    print('이메일 형식이 아닙니다')

print(email)
