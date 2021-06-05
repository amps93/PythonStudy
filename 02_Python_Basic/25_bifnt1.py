#any, all
print(all([0,1,2,3]))
print(any([0,1,0]))
print(any([0,'',0]))
print(any([0,[],0]))

#ascii code value : chr(x)
print(chr(65)) #A
print(chr(97)) #a

#ascii code : ord(c)
print(ord('a'))
print(ord('\n'))
print(ord(' '))
print(ord('\t'))
print(ord('\\'))

#divmod(a,b) : (몫, 나머지)
print(divmod(7,3))

#eval() : 입력받은 문자열을 알맞은 자료형으로 바꿔줌
print(eval('13.5'))
print(type(eval('13.5')))
print(eval('3+5'))

#help()
help(print)