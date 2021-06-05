list1 = [1,2,3]
list2 = [2,1,3]

# # == != < >
print(list1 ==list2)
print(list1 != list2)
print(list1 > list2)

#2차원 리스트
list3 = [[1,2,3],[4,5,6],[7,8,9]]
list4 = [[1,2,3],[1,2],[1,3,4,5]]
print(list3)

for i in list3:
    print(i)

for i in list4:
    for j in i:
        print(j, end=' ')
    print()

print(list3[1][1])