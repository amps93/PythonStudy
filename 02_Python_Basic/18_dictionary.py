d = {1: 'a', 2: 'b', 3: 'c'}
print(d)
print(d[1]) #key값 사용

d2 = {'name': 'Lee', 'tel': '010-1234-5678'}
print(d2['name'])

#딕셔너리에 요소 추가
d[4] = 'f'
print(d)

d2['address'] = '강남구'
print(d2)

d3 = {'name': 'daum',
      'url': 'www.daum.net',
      'userid': 'dm',
      'pw': 1234
      }

#keys, values, items
d3_Key = d3.keys()
print(type(d3_Key))
print(d3_Key)
print(list(d3_Key))

d3_values = d3.values()
print(d3_values)
print(list(d3_values))

d3_items = d3.items()
print(d3_items)
print(list(d3_items)[0])

for key in d3.keys():
    print(key)

#get
print(d3['name'])
# print(d3['add']) #오류

print(d3.get('url'))
print(d3.get('add')) #오류 대신 None 노출
print(d3.get('add','not exist')) #오류 대신 not exist 노출

k = 'link'

if d3.get(k) is None:
    print(k + '에 대한 데이터가 없습니다.')

#in / not in
print('link' in d3)
print('link' not in d3)

print('name' in d3)

#zip() / comprehension
y = [x**2 for x in (2,3,4)]
print(y)
z= {x:x**2 for x in (2,3,4)}
print(z)