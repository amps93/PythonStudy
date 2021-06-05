def even(x):
    return x%2==0

result = filter(even,[2,4,6,8,1,3,5,7])
print(list(result))

