# # 직원 - 아이디 이름 기본급
# # 정규직 - 계약직 - 인턴
# # 정규직 - 보너스 계약직 - 시간당 급여 인턴-고정수당

# class employee:
#     def __init__(self,Id,name,pay_base):
#         self.Id=Id
#         self.name=name
#         self.pay_base=pay_base
    
#     def __str__(self):   #str이 뭐임????/
#           return f'이름: {self.name}, 아이디: {self.Id}, 기본급: {self.pay_base}'

# class real_employee(employee):

#     def __init__(self,Id,name,pay_base,bonus):
#      super().__init__(Id, name, pay_base)   # employee.__init__(self, Id, name, pay_base)
#      self.bonus = bonus
#      self.total_pay= pay_base+bonus
#      print(f'정규직의 수입은 {self.total_pay}입니다')
    
#     def __str__(self):
#        return (f"[정규직] 이름: {self.name}, 아이디: {self.Id}, "
#                 f"기본급: {self.pay_base}, 보너스: {self.bonus}, "
#                 f"총급여: {self.total_pay}")
    
# class yet_employee(employee):
     
#      def __init__(self,Id,name,pay_base,pay_time,time):
#       super().__init__(Id, name, pay_base)   # employee.__init__(self, Id, name, pay_base)
#       self.pay_time=pay_time
#       self.time = time
#       self.pay_time = 5000*time
#       self.total_pay= pay_base+pay_time
#       print(f'계약직의 수입은 {self.total_pay}입니다')
     
#      def __str__(self):
#       return(f"[계약직] 이름 : {self.name}, 아이디: {self.Id}, 기본급: {self.pay_base}"
#              f"시간당 급여: {self.pay_time}, 근무시간: {self.time}, "
#                 f"총급여: {self.total_pay}")
      
# class intern(employee):
   
#    def __init__(self,Id,name,pay_base,pay_fixed):
#       super().__init__(Id, name, pay_base)   
#       self.pay_fixed=pay_fixed
#       self.total_pay= pay_base+pay_fixed
#       print(f'인턴직의 수입은 {self.total_pay}입니다')

#    def __str__(self):
#        return(f"[인턴직] 이름 : {self.name}, 아이디: {self.Id}, 기본급: {self.pay_base}"
#              f"고정수당: {self.pay_fixed}, 총급여: {self.total_pay}")
    
# r = real_employee('R01', '홍길동', 2000000, 300000)
# y = yet_employee('C01', '김철수', 1500000, 5000, 20)
# i = intern('I01', '이영희', 1200000, 200000)
# print(r)  
# print(y)
# print(i)
# --------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------

# 직원 Employee - 아이디,이름,기본급
class Employee:
    def __init__(self,id,name,base_salary):
        self.id = id
        self.name = name
        self._base_salary = base_salary  # private의 의미로 사용
    @property
    def base_salary(self):
        return self._base_salary
    @base_salary.setter
    def base_salary(self, money):
        if money > 0:
            self._base_salary = money
        else:
            raise ValueError('금액은 양수입니다. 마이너스 불가')
    def emp(self):
        print('직원클래스')

    def __str__(self):
        return f'{self.name} : {self.id}, {self.base_salary}'
    
# 정규직 FullTimeEmployee- 보너스
class FullTimeEmployee(Employee):
    def __init__(self, id, name, base_salary,bonus):
        super().__init__(id, name, base_salary)
        self.bonus = bonus
    # bonus도 마이너스 입력 불가        
    def __str__(self):
        return super().__str__() + f', {self.bonus}'
    def fte(self):
        print('정규직 클래스')
# 계약직 PartTimeEmployee- 시간당 급여, 기본급 없음
class PartTimeEmployee(Employee):
    def __init__(self, id, name, hourly_rate, hours):
        super().__init__(id, name, 0)
        self.hourly_rate = hourly_rate
        self.hours = hours
    # hourly_rate  hours  : getter setter
    def __str__(self):
        return f'{self.name} {self.id} {self.hourly_rate} {self.hours}'
    def pte(self):
        print("계약직 클래스")

# 인턴 Intern - 고정수당
class Intern(Employee):
    def __init__(self, id, name, fixed_salary):
        super().__init__(id, name, 0)
        self.fixed_salary = fixed_salary
    def __str__(self):
        return f'{self.name} {self.id} {self.fixed_salary}'
    def int(self):
        print('인턴클래스')

# 정규직 직원, 계약직, 인턴을 모두 리스트에 섞어서 객체를 저장
# emp = [
#     FullTimeEmployee(),
#     ...
#     ...
#     ...
#     ...
#     ..
# ]
# emp에 들어있는 직원이 각각 어떤클래인지 순환을 이용해서 각 클래스의 int,pte 메소드 호출
class Intern(Employee):
	def __init__(self, emp_id, name, allowance):
		super().__init__(emp_id, name, 0)
		self.allowance = allowance
	def get_pay(self):
		return self.allowance
	def __str__(self):
		return f"[인턴] {self.emp_id} {self.name} 급여: {self.get_pay()} (고정수당: {self.allowance})"

# 다양한 직원 객체를 리스트에 저장
emp = [
	FullTimeEmployee('F001', '홍길동', 3000000, 500000),
	FullTimeEmployee('F002', '김철수', 2800000, 400000),
	PartTimeEmployee('P001', '이영희', 20000, 80),
	PartTimeEmployee('P002', '박민수', 18000, 100),
	Intern('I001', '최지우', 1000000),
	Intern('I002', '정해인', 900000)
]

# 직원 정보 출력
for e in emp:
	print(e)