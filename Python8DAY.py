예제1번
friends=['joseph','glenn','sally']
for friend in friends :
    print('happy new years',friend)
#예제2
for i in range(len(friend)):
    friend=friends[i]
    print('happy new years',friend)
#예제 3번

han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()#rstrip 우측으로 빈칸없애기
    wds = line.split()#split 문장 나누기

    if len(wds) < 3 or wds[0] != 'From' :
        continue
    print(wds[2])