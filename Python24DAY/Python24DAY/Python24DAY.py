#내장함수
print(abs(3))#abs 는 그ㅡ숫자의 절대값을 보여줌
all([1,2,3])
all([1,2,3,0])#all은 거짓과 참을 나눠줌
any([1,2,3,0])#any는 x중 하나라도 참이있으면 true를 주고 x가 거짓말일때만 fales를 돌려준다
divmod(7,3)#나눈 몫과 나머지를 알려줌
for i in enumerate(['body','foo,','bar']): #enumerate 는 열거 하다라는 뜻이다. 객체를 돌려준다(리스트,튜플,문자열)
    print(i,name)
eval(1+2)
eval('he'+'llow')
eval('divmod(4,3)')#eval는실행가능한문자열을 입력으로 받아 문자열을 실행한 결과 값을 돌려주는 함수이다
hex(234)#hex는 정수 값을 입력받아 16진수로 변환하여 돌려주는 함수이다.
a=3
id(3)#id는 객체를 입력받아 객체의 고유 주소값을 돌려주는 함수이다.
id(a)
b=a
id(b)
a=input()#input 은 사용자 입력을 받는 함수이다.
print(a)
int('3')#int(x)는 문자열 형태의 숫자나 ㅅ소수점이있는 숫자등을 정수로 바꾸주는 함수
int('3.4')
len("python")#입력값의 길이를 돌려주는 함수이다.
len([1,2,3])
len((1,'a'))
list("python")#반복가능한 자료형 s를받아 리스트로 만들어 돌려주는 함수이다.
