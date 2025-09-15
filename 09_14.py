# class student:
#     def hello(self):
#         print(f'안녕하세요 {self.name}님?')

# s1=student()
# s1.name = "홍길동"
# s1.hello()

# class Car:

#     def __init__(self,brand,year):
#         self.brand = brand
#         self.year = year

#     def info(self):
#          print(f'브랜드 : {self.brand}, 출시년도 : {self.year}')


# c1 = Car("현대", 2000)
# c1.info()

# class Student:
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score 
    
#     def is_pass(self):
#         if self.score >= 60:
#             print (f'{self.name}: 합격')
#         else:
#             print (f'{self.name}: 불합격')

# s1 = Student("홍길동",70)
# s1.is_pass()

# s2 = Student("임꺾정",40)
# s2.is_pass()

# class Cart:
#     def __init__(self):
#         self.items = []
   
#     def add_item(self,item):
#         self.items.append(item)
    
#     def show_items(self):
#         print(self.items)
    
# cart = Cart()
# cart.add_item("사과")
# cart.add_item("바나나")
# cart.show_items()
        
# class BankAccount:
#     def __init__(self,owner,balance=0):
        
#         self.owner = owner
#         self.balance = balance
    
#     def deposit(self,amount):
#         self.balance += amount 
#         print(f'{amount}원 입금완료')

#     def withdraw(self,amount):
#         if self.balance>= amount:
#            self.balance-= amount
#            print(f'{amount}원 출금완료')
#         else:
#             print('잔액부족')

#     def check_balance(self):
#         print(f'현재 잔액: 000원')

# acc = BankAccount("홍길동")
# acc.deposit(1000)
# acc.withdraw(500)
# acc.check_balance()

class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price
    
    def info(self):
        print(f'제목:{self.title}, 저자:{self.author}, 가격:{self.price}')

class Library:
    def __init__(self):
        self.books=[]
    
    def add_book(self,book):
        self.books.append(book)
    
    def show_books(self):
        if not self.books:
            print("도서관에 책이 없음")
        else:
            for book in self.books:
                book.info()
    
    def discount_all(self,rate):
        for book in self.books:
            book.price = int(book.price * (1-rate/100))
    
    def find_book(self,title):
        for book in self.books:
            if book.title == title:
               book.info()
               return
            else:
                print("해당책이 없습니다")

lib = Library()

b1 = Book("파이썬 기초", "홍길동", 20000)
b2 = Book("알고리즘 입문", "이몽룡", 25000)

lib.add_book(b1)
lib.add_book(b2)

lib.find_book("파이썬 기초")
# 출력 → 제목:파이썬 기초, 저자:홍길동, 가격:20000원

lib.find_book("C언어 입문")