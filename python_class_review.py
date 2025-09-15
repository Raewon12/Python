# Python 클래스와 객체지향 프로그래밍 복습
# 작성일: 2025-09-15

'''
1. 클래스 기본
- class 키워드로 정의
- 객체의 설계도
- 속성(변수)과 메서드(함수)를 포함
'''

# 기본 클래스 정의
class Car:
    # 클래스 변수 (모든 인스턴스가 공유)
    total_cars = 0
    
    # 생성자 메서드
    def __init__(self, brand, model):
        # 인스턴스 변수 (각 객체별로 독립적)
        self.brand = brand
        self.model = model
        Car.total_cars += 1
    
    # 인스턴스 메서드
    def display_info(self):
        return f"{self.brand} {self.model}"

# 객체 생성과 사용
car1 = Car("현대", "소나타")
car2 = Car("기아", "K5")

print(car1.display_info())
print(f"총 자동차 수: {Car.total_cars}")

'''
2. 클래스 변수 vs 인스턴스 변수
- 클래스 변수: 모든 인스턴스가 공유
- 인스턴스 변수: 각 객체별로 독립적
'''

class Student:
    # 클래스 변수
    school_name = "파이썬 고등학교"
    
    def __init__(self, name):
        # 인스턴스 변수
        self.name = name

# 클래스 변수 접근
print(Student.school_name)  # 모든 학생이 같은 학교

# 인스턴스 변수 접근
student1 = Student("홍길동")
student2 = Student("이순신")
print(student1.name)  # 각자 다른 이름

'''
3. 상속(Inheritance)
- 기존 클래스의 속성과 메서드를 물려받음
- 코드 재사용성 증가
'''

# 부모 클래스
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

# 자식 클래스
class Dog(Animal):
    def speak(self):
        return f"{self.name}가 멍멍!"

class Cat(Animal):
    def speak(self):
        return f"{self.name}가 야옹!"

dog = Dog("멍멍이")
cat = Cat("냥이")
print(dog.speak())
print(cat.speak())

'''
4. 캡슐화(Encapsulation)
- 정보 은닉
- private 변수 (_변수명 or __변수명)
- property 데코레이터
'''

class BankAccount:
    def __init__(self):
        self._balance = 0  # protected 변수
        self.__password = "1234"  # private 변수
    
    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, value):
        if value >= 0:
            self._balance = value
        else:
            raise ValueError("잔액은 0보다 작을 수 없습니다")

account = BankAccount()
account.balance = 1000  # setter 사용
print(account.balance)  # getter 사용

'''
5. 다형성(Polymorphism)
- 같은 이름의 메서드가 다른 기능을 하는 것
- 메서드 오버라이딩
'''

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

# 다형성 활용
shapes = [Rectangle(10, 20), Circle(5)]
for shape in shapes:
    print(f"면적: {shape.area()}")

'''
6. 특수 메서드
- __str__: 문자열 표현
- __len__: 길이 반환
- __eq__: 객체 비교
'''

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

book1 = Book("파이썬 기초", "홍길동")
book2 = Book("파이썬 기초", "홍길동")

print(str(book1))  # __str__ 호출
print(book1 == book2)  # __eq__ 호출

'''
7. 추상 클래스
- from abc import ABC, abstractmethod
- 추상 메서드를 포함한 클래스
- 직접 인스턴스화할 수 없음
'''

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

class Bicycle(Vehicle):
    def start(self):
        return "페달을 밟습니다"
    
    def stop(self):
        return "브레이크를 잡습니다"

# vehicle = Vehicle()  # 오류: 추상 클래스는 인스턴스화할 수 없음
bike = Bicycle()  # OK
print(bike.start())