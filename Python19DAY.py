#1번 문제 주어진 자연수가 홀수인지 짝수인지 판별해주는 함수 (is_odd)를 작성해보자
def is_odd(number):
    if number%2==1:
        return True
    else:
        return False
#입력으로 들어노는 모든 수의 평균 값을 계산해주는 함수를 작성해보자.

def avg_numbers(*args):
    result=0
    for i in args:
        result+=1
    return (result/len(args))
    avg_numbers(1,2)


#다음은 두개의 숫자를 입력받아 더하여 돌려주는 프로그램이다.
input1=int(input("첫번째 숫자를 입력하세여:"))
input2=int(input("두번쨰 숫자를 입력하세여:"))
total=(input1+input2)
print("두수의 합은%s 입니다."%total) #소수도 가능하고 정수도 가능하게 %s 를 사용한다.

#사용자의 입력을 파일에 저장하는 프로 그램을  작성해보자
user_input=input("저장할 내용을 입력하세여:")
f=open('txt.txt','a')# 내용을 추가하기 위해'a'사용
f.write(user_input)
f.write("\m")#입력한 내용을 줄단위로 구분하기위해 줄바꿈 문자를 삽입
f.close
#다음과 같은 내용을 지닌 파일 test.txt가 있다. 이파일의 내용중 'java'라는 문자열을 'python'으로 바꾸어서 젖ㅇ해보자 
f=open('test.txt','r')
body=f.read()
f.close()
body=replace("java","python")
f=open('test.txt','w')
f.write(body)
f.close()