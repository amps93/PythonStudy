
name = ''

def inputName():
    global name
    name = input('이름 : ')

def getName():
    if name == '':
        return '이름 없음'
    else:
        return name

def main():
    inputName()
    print(getName())


if __name__=='__main__':
    main()