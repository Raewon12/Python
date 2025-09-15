import random
class Person:
    def __init__(self,name,age):
        self.name = name # private 변수로 설정
        self._age =age
    @property # 함수를 변수처럼 쓰고 싶다.. 함수 이름만 가지고 호출하게겠다.
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        self._age=value


p1 = Person("홍길동",20)
print(p1.age)
p1.age = 30
print(p1.age)
print(p1.name)
del p1.name
print(p1.name)