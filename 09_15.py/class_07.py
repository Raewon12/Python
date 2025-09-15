#기본 클래드 생성
class Review:  
    # 클래스 변수 생성
    count=0
    # 생성자 메소드 -> 객체 생성할때 자동으로 호출 되는것 ( 내가 부르는게 아니라 사건이 발생하면 자동으로 호출 ) 이벤트 함수
    def __init__(self, name="",num=0):
        self.name= name
        self.num = num
        Review.count += 1

    # 인스턴스 생성
r1 =Review('홍길동',100) 
r2 =Review()
# 인스턴스 변수 변경
r1.name = "첫번째 리뷰" 

print(f'r1 인스턴스 변수 : {r1.name} / r2 인스턴스 변수 : {r2.name} ')
print(f'클래스 변수 : {Review.count} / r1 클래스 변수:{r1.count}') 
#인스턴스 변수는 객체 중심으로 써라


# 추상화 : 