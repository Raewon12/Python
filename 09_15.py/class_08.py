# 학생클래스 생성
# 인스턴스 변수 : 이름 국 영 수
# 인스턴스 매서드: 총점, 평균, 학점

class Student:
    def __init__ (self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total_score = self.kor + self.eng + self.math  
        self.avg = self.total_score / 3
    
    def total(self):
        self.total_score = self.kor + self.eng + self.math
        print(f'총점은 {self.total_score}입니다')
        return self.total_score
    
    def average(self):
         print(f'평균은 {self.avg:.2f}입니다')
         return self.avg
    
    def grade(self):
        if self.avg >= 70:
            return 'A'
        elif self.avg >= 60:
            return 'B'
        elif self.avg >= 50:
            return 'C'
        else:
            return 'F'
        


s1 = Student("홍길동", 80, 70, 90)
s1.total()
s1.average()
