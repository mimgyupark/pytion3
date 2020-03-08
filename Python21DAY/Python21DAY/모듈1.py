
#모듈1.py
def add(a,b):
    return a+b
def sub(a,b):
    return a-b

#모듈 실행 방법
#impor 사용 하기 
import 모듈1 #import 모듈이름
print(모듈1.add(3,4))
#from사용하기
from 모듈1 import add#from 모듈이름 import 모듈함수
print(add(3,4))
#from으로 모듈 함수 두개사용하는방법
from 모듈1 import add,sub
print(sub(5-2))
