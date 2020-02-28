#딕셔 너리 {} 로 되어있다 딕셔너리는 key 와 value 로 구성되어있다
#.keys ( ): key를 list로 만들기
#.values ( ): value를 list로 만들기
#.items ( ): key, value 쌍을 반환
#.clear ( ): key, value 쌍을 모두 삭제
#.get ( x , '디폴트'): x에 해당하는 key 값이 없을 때 디폴트 값을 가져감
#in: 해당 key가 있는지 조사
#딕셔너리 dic 의 정보
dic={'key':['name','phone','birth'],'value':['pey','01072051532','0901']}
print(dic)
print('_'*35)
#딕셔너리 쌍추가 삭제하기
a={1:'a'}
a[2]='b'
print(a)
del a[1]
print(a)
print('_'*35)
#딕셔너리에서 key를 사용해 value 얻기
grade={'pey':10,'julliet':99}
print(grade['pey'])
print('_'*35)
#딕셔너리에서 key가 중복되었을때는 하나가 무시된다
#딕셔너리에서 key에 리스트가[] 들어올수없다.
#key리스트 만들기
a={'name':'pay','phone':'01072051532','birth':'980901'}
a.keys()#a의 key만 모아서 dict_keys객체를 돌려준다
print(a.keys())
print('_'*35)
#키를 계속 뽑아줌
a={'name':'pay','phone':'01072051532','birth':'980901'}
for k in a.keys:
    print(k)
print('_'*35)
#dict_keys 객체를 리스트로 변환
print('_'*35)
print(list(a.keys()))
#value 리스트 만들기
print('_'*35)
print(a.value())
print('_'*35)
#itmes 함수 key와 value 의 쌍을 튜플로 묶은 값을 돌려줌
print(a.items())
#get key로 value 얻기 
print('_'*35)
print(a.get(name))# get을 사용할경우 없는 키일경우 오류가 아니라 none 없다고 뜬다 get 활용을하자
print('_'*35)
#key:value 쌍 모두 지우기(clear)
a.clear()
print(a)
print('_'*35)
#집합 자료형 특징 1.중복을 허용 하지 않는다, 2.순서가 없다(set)
s1=set([1,2,3])
print(s1)
s2=set("hello")
print(s2)
print('_'*35)
#집합 자료형 리스트와 튜플로 변화
s1=set([1,2,3])
l1=list(s1)# 집합 자료형 set를 리스트로 변환
print(l1)
t1=tuple(s1)#집합 자료형 set를 튜플로 변환
print(t1)
print('_'*35)
#교집합 차집합 합집합 구하기
s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])
print(s1&s2)#교집합
print(s1.intersection(s2))#교집합
print(s1|s2)#합집합
print(s1.union(s2))#합집합
print(s1-s2)#차집합
print(s1.defference(s2))#차집합
print('_'*35)
#값1개 추가하기 (add)
s1=set1([1,2,3])
s1.add(4)
print(s1)
#값여러개 추가하기 (update)
print('_'*35)
s1=set([1,2,3,])
s1.update([4,5,6,])
print(s1)
#특정값 제거하기 (remove)
print('_'*35)
s1=set([1,2,3])
s1.remove(2)
print(s1)