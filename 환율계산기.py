#3개 나라 환율 계산기 (만들고싶은)
print('미국,중국,영국 환전 계산기')
kr=input('가지고있는 한국돈을 입력하시오')
try:
    kr=float(kr)
except:
    print('ERROR')
list=['미국','중국','영국']
choice=input('환전하고 싶은 나라를 입력하시오')
if choice=='미국':
    a=float(kr/1187)
    print(a,'USD입니다.')
elif choice=='중국':
    b=float(kr/170)
    print(b,'CNY입니다.')
elif choice=='영국':
    c=float(kr/1,536)
    print(c,'GBP입니다.')
else:
    print('ERROR')

