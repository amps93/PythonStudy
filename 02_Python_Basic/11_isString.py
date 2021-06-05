#isalpha() / isdigit() / isspace() / isalnum() / islower() / isupper()

text = '123456num'
print(text.isdigit())
print(text.isalpha())
print(text.isdigit())
print('   '.isspace())
print('Abc'.islower())
print('Abc'.isupper())


a=input('이메일 입력 : ')
alphas = digits = space = others = 0

for c in a:
    if c.isalpha():
        alphas+=1
    elif c.isdigit():
        digits+=1
    elif c.isspace():
        space+=1
    else:
        others+=1

print(alphas,digits,space,others)