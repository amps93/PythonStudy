#3
def input_member(input_filename):
    while True:
        name = input('멤버를 입력하세요.(종료는 q) : ')
        if name == 'q':
            return
        with open(input_filename, 'a', encoding='utf-8') as f:
            f.write(name+'\n')

def output_member(output_filename):
    with open(output_filename, 'r', encoding='utf-8') as f:
        data = f.read()
    print(data)


def main():
    while True:
        order = input('저장 1, 출력 2, 종료 q : ')
        if order == '1':
            input_filename = input('멤버 명단을 저장할 파일명을 입력하세요. : ')
            input_member(input_filename)
        elif order == '2':
            output_filename = input('멤버 명단이 저장된 파일명을 입력하세요. : ')
            output_member(output_filename)
        elif order == 'q':
            break







