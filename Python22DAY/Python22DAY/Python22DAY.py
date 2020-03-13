#예외처리
#execpt[발생오류[as오류 메세지 변수]]:
try:
    4/0
except ZeroDivisionEorror as e:
    print(e)
f=open('foo,txt','w')
try:
    #무언가를 수행한다,
finally:
    f.close()
#여러개의 오류 처리
try:
    a=[1,2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌수 없습니다.")
except IndexError:
    print("인덱싱 할수 없습니다")
#오류 회피하기
try:
    f=open("나없는 파일",'r')
except FileNotFoundError:
    pass
#민규야 제발 class이해좀하자 빡대가리야
