
#클래스
result=0
def add(num):
    global result
    result+=num#result=result+num
    return result
print(add(3))
print(add(4))
#계산기 두개
result1=0
result2=0 
def add1(num):
    global result1
    result1+=num
    return result1
def add2(num):
    global result2
    result2+=num
    return result2
print(add1(2))
print(add1(3))
print(add2(3))
print(add2(4))
#계산기1이 계산기2에 아무 영향을 끼치지 않는다
class Caculator:
    def __init__(self):
        self.result=0
    def add(self,num):
        slef.result +=num
        return self.result
cla1= Caculator()#cla1을 객체라고 부른다
cla2= Caculator()
#사칙 연산 클라스로 더하기 계산기 만들기
class Fourcal():
    def setdata(self,first,second):
        self.first=first
        self.second=second
    def add(self):
        result=self.first+self.second
        return result
    def mul(self):
        result=self.first*self.second
        return result
    def sub(self):
        result=self.first-self.second
        return result
    def div(self):
        result=self.first/self.second
        return result
a=Fourcal()
b=Fourcal()
a.setdata(4,2)
b.setdata(3,2)
print(a.add())
print(b.add())
print(a.mul())
print(b.sub())
#사칙 연산 클라스 로  더하기계산기 두개 만들기
class Fourcla():
    def setdata(self,first,second):
        self.first=first
        self.second=second
a=Fourcal()
a.setdata(3,7)
print(a.first)#두개의 다른 객체 변수가 생긴다 독립적인 값을 유지한다,
b=Fourcal()
b.setdata(4,5)
print(b.first)

#좀 다른거
class Fourcal():
    def __init__(self,first,second):#생성자 를 만든다 이해가 어렵다 다시보자
        self.first=first
        self.second=second
    def setdata(self,first,second):
        self.first=first
        self.second=second
    def add(self):
        result=self.first+self.second
        return result
    def mul(self):
        result=self.first*self.second
        return result
    def sub(self):
        result=self.first-self.second
        return result
    def div(self):
        result=self.first/self.second
        return result
a=Fourcal(4,2)#이렇게 바뀐다 위에꺼처럼 하면 오류가 뜬다
b=Fourcal(5,6)
print(a.add())
print(b.add())
print(a.mul())
print(b.sub())
