#예제 1번
a="Life is too short, you need python"
if "wife" is a: print("wife")
elif "python" in a and "you" not in a: print("pyhton")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")
#예제2번 1000까지의 3의배수의 합
result=0
i=1
while i <= 1000:
    if i%3==0:
        result += i
    i += 1
    break
print(result)

#예제 3번 while 문
i=0
while True:
    i+=1
    if i>5: break
    print(i*'*')
#예제 4번 for 문을 사용하여 1부터 100까지의 숫자를 출력해보자
for i in range(1,101):
    print(i)
#예제5번 학급에 총 10명의 학생이 있다. 이학생들의 중간고사 점수는 다음과 같다. 평균점수를 구하라
#[70,60,55,75,95,90,80,80,85,100]
A=[70,60,55,75,95,90,80,80,85,100]
total=0
for score in A:
    total += score
average=score/len(A)
print(average)
#예제 6번 
number=[1,2,3,4,5]
result=[n*2 for n in number if n%2==1]
print(result)