# isinstance()함수
# 객채가 특정 클래스의 인스턴스(객체)인지 확인하는데 사용합니다.
# 사용하는 이유
# 1. 타입확인 :함수나 메서드가 특정 클래스의 인스턴스를 기대할떄 이를 확인
#2. 다형성 지원: 상속 관계에 있는 클래스들 간에 공통된 인터페이스를 제공할때,

class Student:
    def study(self):
        return "공부 중입니다."

class Teacher:
    def teach(self):
        return "가르치는 중입니다."

#리스트에 어떤 객체가 있는지 모를떄 특정 인스턴스만 기대할 수 없다.

peoples = [Student(),Teacher(),Student()]
del peoples[0]
if isinstance(peoples[0],Student):
    print(peoples[0].study())
else:
    print(peoples[0].teach())

peoples[0].teach()