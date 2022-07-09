# 클래스 초기화 함수, __init__() 재정의
class MyClass:
    def __init__(self, name):     # 초기화 함수 재정의
        self.name = name

    def sayHello(self):
        hello = "Hello, " + self.name + "\t It's Good day !"
        print(hello)

    def sayGoodbye(self):
        hello = "Seeya, " + self.name + "\t Bye !"
        print(hello)

# 객체 생성, 인스턴스화
# myClass = MyClass()
myClass = MyClass('채영')
myClass.sayHello()

myClass2 = MyClass('효정')
myClass2.sayHello()
myClass2.name = '진수'
myClass2.sayGoodbye()

