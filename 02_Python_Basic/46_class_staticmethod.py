#정적메소드 : self를 통하지 않고 바로 클래스가 메소드 호출
#@staticmethod : 함수의 데코레이터 -> 정적메소드로 정의한다 표시
class CalC:
    @staticmethod
    def add(a,b):
        return a+b

    @staticmethod
    def sub(a, b):
        return a - b

    @staticmethod
    def mul(a, b):
        return a * b

    @staticmethod
    def div(a, b):
        return a / b

