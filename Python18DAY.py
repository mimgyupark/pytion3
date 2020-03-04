#def
def add(a,b):
    return(a+b)
a=3
b=4
c=add(a,b)
print(c)

#def 예시2 일반 함수의 전형적인예이다.
def add (a,b):
    result=a+b
    return result
#add 는 ㄷ입력값을 받아서 서로 더한 결과값을 돌려준다
a=add(3,4)
print(a)
#def 예시 #결과 값이 없다.! 오로지 결과값은 return 으로 만받을수있다 이문제에서는 print로 수행만 했을뿐이다.
def add(a,b):
    print("%d,%d의합은%이다."%(a,b,a+b))
    add(7,8)
#여러개의 입력값을 받는 함수 만들기
def add_many(*args):
    result=0
    for i in args:
        result=result+1
    return result
#키워드 파라미터 딕셔너리에 저장되는 형태
def print_kwargs(**kwargs):
    print(kwargs)#{'a',:1}
#lambda
add=lambda a,b:a+b
result=add(3,4)
print(result)
#input 사용자값입력하기
a=input("파일이름을 입력하시오")
print(a)
#파일 읽고 쓰기
f=open("C:/doit/새파일.txt",'w')
for i in range(1,11):
    data="%d줄입니다.\n"%i
    print(data)
#파일 읽기
f=open("C:/doit/새파일.txt",'r')
line=f.readline()
print(line)
f.close
