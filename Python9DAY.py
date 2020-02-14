fname=input('파일 이름을 입력하시오')
if len(fname) < 1: fname='intro.txt'
hand=open(fname)

di=dict()
for line in hand:
    line=line.rstrip()
    word=line.split()
    for w in word:
        di[w] = di.get(w,0)+1


largestt = -1
theword = None
for k, v in di.items() :
    print(k,v)
    if v > largest : 
        largest = v
        theword = k
        
print('Done', theword, largest)
       