'''
가우스 조던 소거법을 통한 연립방정식 계산

행렬방정식의 해 구하기

y -3z = -5

2x + 3y -z = 7

4x + 5y - 2z = 10

https://m.blog.naver.com/PostView.nhn?blogId=justant&logNo=20208491220&proxyReferer=https:%2F%2Fwww.google.com%2F
'''
import numpy as np
import copy


# x, y, z 순서대로 a 행렬 생성 - * .0을 붙이지 않고 정수 형태로 만들경우 뒷 부분의 나눗셈 부분에서 정수로 떨어
a = np.array([[0.0, 1.0, -3.0], [2.0, 3.0, -1.0], [4.0, 5.0, -2.0]])
b = np.array([[-5.0], [7.0], [10.0]])

# 확인용 함수
def check(a, b):
    print(a)
    print('=================')
    print(b)

# 행렬 내부 위치 바꾸는 함수 - deepcopy를 쓰지 않을 경우 얕은복사로 인하여 tmp의 값이 변화됨
def change(inp_list, inp1, inp2):
    tmp = copy.deepcopy(inp_list[inp1])
    inp_list[inp1] = inp_list[inp2]
    inp_list[inp2] = tmp
    result = inp_list
    return inp_list

# 1열 2열 위치 변경
a = change(a, 0, 1)
b = change(b, 0, 1)

# 1열 1행을 1로 만들기 위해(x 값을 1로 만들기 위해) 2씩 나눠줌
a[0] = a[0] / 2
b[0] = b[0] / 2
check(a, b)
print()

# 3행 = 3행 - (1행 * 4)
a[2] = a[2] - (a[0] * 4)
b[2] = b[2] - (b[0] * 4)
check(a, b)
print()

# 3행 = 3행 + 1행
a[2] = a[2] + a[1]
b[2] = b[2] + b[1]
check(a, b)
print()

# 3행 = 3행 / (-3)
a[2] = a[2] / (-3)
b[2] = b[2] / (-3)
check(a, b)
print()

# 2행 = 2행 + (3행 * 3)
a[1] = a[1] + (a[2] * 3)
b[1] = b[1] + (b[2] * 3)
check(a, b)
print()

# 1행 = 1행 + (3행 * (1/2))
a[0] = a[0] + (a[2] * 1/2)
b[0] = b[0] + (b[2] * 1/2)
check(a, b)
print()

# 1행 = 1행 - (2행 * (3/2))
a[0] = a[0] - (a[1] * (3/2))
b[0] = b[0] - (b[1] * (3/2))
check(a, b)
print()

#  x = -1, y = 4, z = 3
check(a, b)
print()


### Numpy Solver
print('Numpy Solver')
A = np.array([[0.0, 1.0, -3.0], [2.0, 3.0, -1.0], [4.0, 5.0, -2.0]])
B = np.array([[-5.0], [7.0], [10.0]])

C = np.linalg.solve(A, B)

print(C)
type(C)