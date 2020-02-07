
#CHEPER.try와except를 이용한 주급 계산기
time=input('일하신 시간을 적으세요')
pay=input('현재 받고 계신 시급을 입력하세요')
try:
    ti=float(time)
    pa=float(pay)
except:
    print('Error, please enter numeric input')
    quit()
if ti>52:
    #print("추가근무")
    주급=ti*pa
    추가근무시간=(ti-40)*(pa*0.5)
    a=주급+추가근무시간
else:
    a=(ti*pa)
print('_______________________________')
print('당신의 월급은',a,'원입니다.')
print('_______________________________')
