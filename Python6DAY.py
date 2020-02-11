#파이썬공부 6일차 문자열을 찾고 그문자열 을 바꾸는 함수 검색


str='대한민국 독도는 우리땅'
ipos=str.find('국')#국이라는 단어가 어디있는지 찾는
piece=str[ipos+2:]#국이라는 위치에서 두칸이동 한거부터시작한다
print(piece)
print('_____________________')
#len이 무었인가
fruit='banana'
x=len(fruit)#문자의 갯수를 알려주는 len
print(x)
print('_____________________')
#소문자로 바꾸기
print('HI THERE'.lower())
#대문자로 바꾸기
print('hi there'.upper())
#문자를 바꿔줌
a='대한민국 독도는 우리땅'
b=a.replace('독도는','독도는 일본땅이아닌')
print(b)
