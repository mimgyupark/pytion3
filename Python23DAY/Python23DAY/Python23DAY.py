#클래스 3번째 공부
class Person:
    def __init__(self,name,age):#초기자
        self.name=name
        self.age=age 
p1=Person('홍길동',22)
p2=Person('박민규',23)
print(p1.name)
print(p2.name)
print(p2.age)
print(p2.age)
class Person:
    def __init__(self,name,age):#초기자
        self.name=name
        self.age=age 
    def disp(self):
        print(self.name)
        print(self,age)
p1=Person('홍길동',22)
p2=Person('박민규',23)
p1.disp()
p2.disp()
print(p1.name)
#직접 입력하는
class Person:
    def __init__(self,name,age):#초기자
        self.name=input('이름:')
        self.age=int(input('나이:'))
    def disp(self):
        print(self.name)
        print(self,age)
p1=Person()
p2=Person()
p1.disp()
p2.disp()
#여러명을 사용하는것
class Person:
    def __init__(self,name,age):#초기자
        self.name=input('이름:')
        self.age=int(input('나이:'))
    def disp(self):
        print(self.name)
        print(self,age)
li=[]
for i in range(3):
    li.append(person())
for i in range(len(li)):
    li[i].disp()