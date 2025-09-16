# 상속의 정의
# 상속은 기존 클래스의 속성과 메서드를 새로운 클래스를 물려받는것 
#상속이용해서 코드 재사용성 높이고 계층적 관계표현
#기본문법
# class 부모클래스:
#     def 부모메서드(self):
#         print("부모 메서드 호츨")

# class 자식클래스(부모클래스):
#     def 자식메서드(self):
#         print()

#부모 클래스
class Parents:
    def __init__(self,name):
        self.p_name = name
        print('부모생성자')
    def parents_method(self):
        print('부모클래스 메소드')

class Child(Parents):
    def __init__(self,name,age):
        Parents.__init__(self,name) ##### 자식생성자안에서 부모생성자 호출하기
        self.age = age
        print('자식생성자')
    def child_method(self):
        print('자식클래스 메소드')
    
# child 클래스 객체 c
c = Child('홍길동',20)
print(c.p_name,c.age)


