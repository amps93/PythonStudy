total = 0
for i in range(101):
    total += i
print('1~100 합 : {}'.format(total))

total = 0
for i in range(3,21,3):
    total += i
print(total)

total = 0
for i in range(1,21):
    if i%3==0:
        total+=i
print(total)

#문제 1
a= int(input('숫자 1 : '))
b= int(input('숫자 2 : '))
total = 0
if a<b:
    for i in range(a,b+1):
        total += i
else:
    for i in range(b,a+1):
        total += i
print(total)

#문제 2
a = int(input('단을 입력 : '))
for i in range(1,10):
    print('%d * %d = '%(a,i), a*i)

#문제 3
a = int(input('숫자 입력 : '))
for i in range(a,0,-1):
    print(i,end=' ')
print('발사')