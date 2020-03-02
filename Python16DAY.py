#IF문 비교연산자를 사용해야된다 참인지 거짓인지
 #예제1번
money=True
if money:
    print("택시를 타고가라")
else:
    print("걸어가라")
print('-'*18)
 #예제2번
money=2000
if money>=3000:
    print("택시를 타고가라")
else:
    print("걸어가라")
print('-'*18)
# x or y x와y둘중에 하나만 참이면 참이다.
# x and y x와y 모두 참이어야한다,
#not x x가 거짓이면 참이다.

 #예제3번 or문 사용
money=2000
card=True
if money>3000 or card:
    print("택시를 타고가라")
else:
    print("걸어가라")
    print('-'*18)
#in  활용 예제4번
print(1 in[1,2,3])
print('-'*18)
print(1 not in[1,2,3])
print('-'*18)
#튜플과 문자열에 적용한 예이다.
print('a' in ('a','b','c'))
print('-'*18)
print('j' not in 'python')
print('-'*18)
#예제 5번
pocket=['papper','cellphone','money']
if 'money' in pocket:
    print('택시를 타고가라')
else:
    print('걸어가라')
print('-'*18)
#조건문에서 아무일도 하지 않게 설정하고싶다면? pass 사용
pocket=['papper','money','cellphone']
if 'money'in pocket:
    pass
else:
    print('카드를 꺼내라')
print('-'*18)
#조건문에서 elif사용 elif 는 이전 조건문이 거짓일때 수행된다. if,elif,else 모두 사용할때 구조는 똑같다.
pocket=['papper','cellphone']
card=True
if 'money'in pocket:
    print("택시를 타고가라")
elif card:
    print("택시를 타고가라")
else:
    print("걸어가라")
print('-'*18)
#짧게 쓰는방법
pocket=['papper','money','cellphone']
if money in pocket:pass
else: print("카드를 꺼내라")
#조건부 표현식
score=70
if score >=60:
    message="sucess"
else:
    message="failure"
    print(mesaage)
print('-'*18)
# 짧게 쓰는방법
message="succes"if score >=60 else"failire"
print('-'*18)
#while 문 예제
treehit=0
while treehit<10:
    treehit=treehit+1
    print("나무를%d번 찍었습니다다"%treehit)
    if treehit==10:
        print('나무 넘어갑니다')
print('-'*18)
#while 문 예제
coffee=10
money=300
while money:
    print("돈을 받았으니 커피를 줍니다")
    coffee=coffee-1
    print("남은 커피는 %d 개입니다"%coffee)
    break
    if coffee==0:
        print("장사를 종료합니다.")
        break
print('-'*18)
#커피 자판기 프로그램 만들기
cofee=10
while True:
    if money==300:
        print("커피를 제공한다.")
        coffee=coffee-1
    elif money>300:
        print("거스름돈%d를 드리고 커피를 제공한다."%(money-300))
        coffee=coffee-1
    else:
        print("커피를 제공할수 없습니다")
        print("남은 커피량은 %d개입니다."%(coffee))
    if coffee==0:
        print("커피가 다떨어졌습니다 판매가 끝났습니다")
        break
#1부터 10까지의 숫자중 홀수만출력해주는 프로그램
a=0
while a<10: #a 는 10까지 의 숫자
    a=a+1   #10보다 작은 모든 숫자에 1을 더한다,
    if a % 2==0: continue #a를 2로 나눈 나머지값이 0이면 맨처음으로 돌아간다(continue)
    print(a)
#무한 루프 빠져 나오기
while True:
    print("ctrl+c를 눌러야 while 문을 빠져나갈 수 있습니다.")
    break
#for문 과 자주 쓰이는 range문
a=range(10)
print(a)
a=range(1,11)
print(a)
print('-'*18)

#range와 for문을 이용한 구구단
for i in range(2,10):
    for j in range(1,10):
        print(i*j,end=" ")# end 사용이유 해당 결과 값을 출력할때 다음줄로 넘기지 않고 그줄에 계속해서 출력하기위해서 
    print(' ')#다음줄로 가게 하기위해서 2번쨰for문에서


