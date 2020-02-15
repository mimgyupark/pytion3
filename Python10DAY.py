#튜플을 사용한 파일에서 제일 많이 사용된언어를 뽑고 정리해주는 프로그램
fname=input('프로그램이름을 입력하시오:')
if len(fname)<1: fname='intro.txt' #아무거나 치면 intro txt 프로그램에 들어가짐
hand=open(fname)

di=dict()
for line in hand:
    line=line.rstrip()
    words=line.split()
    for word in words:too many values to 
        di[word]=di.get(word,0)+1
tmp = list()
tmp.append([(v, k)for k, v in di.items()])
tmp = sorted(tmp, reverse = True)


for v,k in tmp[:10]:
    print(k,v)
