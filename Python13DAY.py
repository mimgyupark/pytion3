#점프투 파이썬 여태 배운거 심화과정
multiline='''life is too short\n you need pythion'''
print(multiline)
print("="*50)
#\n =문자열 안에서 줄을 바꿀때 사용
#\t =문자열 사이에 탭간격을 줄때 사용
#\\ =문재\를 그대로 표현할때 사용
#\' =작은 따움표를 그대로 사용할때 사용
#\r =캐리지 리턴 
a="pythion"
print(a*2)
#multisring.py
print("="*50)
print('game start')
print("="*50)
b="life is too short you need pythion"
print(b[-2])#뒤에서 두번째
print("="*50)
c=b[0]+b[1]+b[2]+b[3]#문자열 슬랙싱
print(c)
print("="*50)
print(b[0:4])#위와 같은 방법
print("="*50)
print(b[:34])#전체를 슬랙싱
print(b[:])#전체를 슬랙싱
print("="*50)
print(len(b))#문자의 갯수
print("="*50)
c="201713061박민규"#학번
number=c[:9]
name=c[9:]
print(number)
print(name)
print("="*50)
#포매팅 문자열 안에 특정한 값을 바꿔야 할경우에 이것을 가능하게 해주는것이 바로 문자열 포매팅 기법이다.
ex="i eat %d apples," %3
print(ex)
print("="*50)
ex1="i eat %s applles" %"five" #문자 안에는꼭 "" 넣기
print(ex1)
print("="*50)
num=10
day="three"
ex2="i ate %d apples. so i was sick for %s day."%(num,day) # 변수를 둔 포매팅
print(ex2)
print("="*50)
#%s =문자열 (string)
#%d =정수
#%c =문자 1개
#%f =부동 소수
#%d 와 %를 같이 쓸때는 %% 사용
ex3= "Error is %d%%."%98
print(ex3)
print("="*50)
ex4="%10s"%"hi"#전체 길이가10개인 문자열 공간에서 대입되는 값을 오른쪽으로 정렬
print(ex4)
print("="*50)
ex4="%-10sjaine"%'hi'#hi 를 왼쪽으로 정렬후 나머지는 공백
print(ex4)
print("="*50)
ex5="%0.4f" %3.14561234 #소숫점 4자리까지 표현하라
print(ex5)
print("="*50)
#format 함수를 사용한 포매팅 방법 ****중요
ex6="i eat{0} apples". format(3)
print(ex6)
print("="*50)
ex7="I eat{0} apples".format("five")
print(ex7)
print("="*50)
ex8="i ate{0} apples. so i was sick {1}days.".format(num,day) #두개 이상의 값 넣기 #num 과 day 의 변수는 대입 되어있다
print(ex8)
print("="*50)
ex9="{0:^10}".format("hi") #가운대 정렬
print(ex9)
print("="*50)
ex10="{0:@^10}".format("hi") #공백 채우기
print("="*50)
#f 문자열 포매팅 파이썬 3.6 부터 사용가능 함
이름='박민규'
나이=23
ex11=f'나의 이름은 {이름}입니다. 나이는 {나이}입니다.'
print(ex11)
print("="*50)
ex12=f'나의 이름은 {이름}입니다. 나이는 {나이+1}입니다.' #변수에서 더하기가 가능하다
print(ex12)
print("="*50)
#위치 알려주기 find
b="life is too short you need pythion"
print("="*50)
print(b.find('t'))#t 의 위치 찾기 find
print(b.find('k'))#k 의 위치 찾기 만약에 없으면 -1 이 나옴
b="life is too short you need pythion"
print("="*50)
#위치 알려주기 index    find 와의 차이점은 없으면 오류가 생성됨
print(b.index('t'))#t 의 위치 찾기 index
print("="*50)
#문자열 사입 join
#소문자를 대문자로 upper ex)a.upper()
#대문자를 소문자로 (lower)
#왼쪽 공백 지우기(lstrip)
#오른쪽 공백 지우기 (rstrip)
#양 쪽 공백 지우기(strip)
# 문자열 바꾸기 (replace)
a="life is too short"
a=a.replace("life","leg") #문자열 을 바꾼다
print(a)
print("="*50)
#문자열 나누기 (split) 공백을 기준으로 나눠서 리스트에 하나씩 들어가게 된다. ******활용도 높음
a="life is too short"
a=a.split()
print(a)
print("="*50)
#삼중 리스트에서 인덱싱 하기
a=[1,2,['a','b',['life','is']]] #3중 리스트
print(a[2][2][0])#life 를 도출함
print("="*50)
#리스트 길이구하기 (len)함수 사용
a=[1,2,3]
print(len(a))
print("="*50)
#리스트 에서 수정하기
a=[1,2,3]
a[2]=4
print(a)
#리스트 에서 요소 삭제하기
print("="*50)
a=[1,2,3]
del a[1]
print(a)
#리스트에서 요소 한꺼번에 삭제하기
print("="*50)
a=[1,2,3,4,5,6]
del a[2:]
print(a)
print("="*50)
#리스트에 요소 추가
a=[1,2,3,4]
a.append(5)
print(a)
a.append([5,6])
print(a)
print("="*50)
#리스트 정렬 (sort)
a=[1,2,3,4]
a.sort()
print(a)
#리스트 뒤집기 (reverse)
print("="*50)
a=[1,2,3,4]
a.reverse
print(a)
#위치 반환 (index)
print("="*50)
a=[1,2,3,4]
b=a.index(3)
print(b)
print("="*50)
#리스트에 요소 삽입 (isert)
a=[1,2,3]
a=a.insert(0,4)# 0 자리에 4를 삽입
print(a)
print("="*50)
#리스트 요소 제거 (remove)
a=[1,2,3,1,2,3]
a=a.remove(3) #1,2,1,2,3
print(a)
print("="*50)
#리스트 요소 끄집어 내기(pop)  
a=[1,2,3]
a=a.pop()# 맨 마지막 요소를 돌려주고 그요소는 삭제한다
print(a)
print("="*50)
#리스트에 포함된 요소 x 의 개수 세기(count)
a=[1,2,3,1]
a=a.count(1)
print(a)
print("="*50)
#리스트 확장(extend)
a=[1,2,3]
a=a.extend([4,5]) #리스트 값을 리스트대로 추가한다 즉 리스트 확장을 해준다
print(a) #값이 [1,2,3,4,5]로 나온다
print("="*50)
#튜플  튜플은 리스트 와 몇가지점을 제외하고는 리스트와 거의 비슷하며 다른점은 다음과 같다
#리스트는[] 로 둘러 싸지만 튜플은() 로 둘러싼다
#리스트는 그 값의 생성,삭제.수정이 가능 하지만 튜플은 그 값을 바꿀수없다
t1=()
t2=(1,)#1개의 요소를 가질때는 꼭, 를 붙여야한다
t3=(1,2,3)
t4=1,2,3#()를 생략해도 무방하다
t5=('a','b',('ab','cd'))
#(1,2,3)이라는 튜플에 값4를 추가해보아라
a=(1,2,3)# () 이것이 튜플이라는 뜻이다
a=a+(4,)# 1개의 요소를 가질때는 꼭, 를 붙인다
print(a)


