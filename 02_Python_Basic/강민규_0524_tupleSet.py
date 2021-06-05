#1
my_variable = ()

#2
#t=(1,2,3)
#t[0]='a'
#t[0]='a'은 딕셔너리 자료형에서 사용 가능한 문법이다

#3
a = (1,)
print(type(a))

#4
t = 1,2,3,4
#튜플 tuple

#5
t = ('a','b','c')
t = ('A','b','c')
print(t)

#6
interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest = list(interest)
print(interest)

#7
interest = ['삼성전자', 'LG전자', 'SK Hynix']
interest = tuple(interest)
print(interest)

#8
partyA = {"Park", "Kim", "Lee"}
partyB = {"Park", "길동", "몽룡"}

#8-1
print(partyA | partyB)
#8-2
print(partyA & partyB)
#8-3
print(partyA - partyB)
#8-4
print(partyB - partyA)