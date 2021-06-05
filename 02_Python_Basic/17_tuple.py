# t1 = tuple()
# t2 = ()

t1 = (1,2,3)
print(t1)

t2 = 1,3,4
print(t2)

t3 = t1, (5,6,7)
print(t3)

t4 = [1,4],[5,6]
print(t4)

t5 = tuple([1,4]) #리스트를 튜플로 변환
print(t5)

#튜플의 요소 다루기
print(t1[2])
# t1[2] = 10 #오류
# del t1[2] #오류

#index, count
print('-'*50)
tt = 'a','b','c','e','a','d'
print(tt.index('e'))
print(tt.count('a'))

#slicing
t = tt[:]
print(t)
t = tt[1:5]
print(t)
print(tt+tt)
print(tt*2)

#tuple 연습문제
tt = ((1,2,3),(4,5,6),(7,8,9))
print(tt[1][2])

for i in tt:
    print(*i)

for i in tt:
    print()
    for j in i:
        print(j,end=' ')
print()
#tuple 값 추가하기
myTuple = (10,20,30)
myTuple = (10,20,30,40) #재정의
print(myTuple)

myTuple = (10,20,30)
myList = list(myTuple) #리스트로 변환 후 추가
myList.append(40)
myTuple = tuple(myList)
print(myTuple)