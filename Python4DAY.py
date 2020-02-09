#40시간이 넘으면 추가 급여를 지급하는 프로그램 (def사용)
def computepay(hours,rate):
    if hours>40:
        reg=rate*hours
        otp=(hours-40)*(rate*0.5)
        pay=reg+otp
    else:
        pay=hours*rate
    return pay
ch=input('how many works?')
sr=input('enter rate')
a= float(ch)
b= float(sr)
xp=computepay(a,b)
print('pay',xp)

