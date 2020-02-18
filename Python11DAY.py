#정규식 배우기
#정규식을 사용 전 “import re” 가져오기
#^:문장의 시작을 의미한다
#.:어떤 문자 한글자
#*:앞의 문자가 반복 가능하다
#+:앞의 문자가 1번이상 나타남
#\s:공백 문자가 아닌 한개의 문자

#따라서, 다음과 같은 문자열들은 모두 '^X.*:'라는 패턴을 통해 찾을 수 있습니다.
#X-Sieve: CMU Sieve 2.3
#X-DSPAM-Result: Innocent
#X-DSPAM-Confidence: 0.8475
#X-Content-Type-Message-Body: text/plain

#그리고 다음과 같은 문자열들은 '^X-\S+:' 패턴으로 찾을 수 있으며,
#X-Sieve: CMU Sieve 2.3
#X-DSPAM-Result: Innocent

#다음의 문자열은 'X-'와 ':' 사이에 공백 문자가 아닌 문자가 포함되지 않았기 때문에 '^X-\S+:' 패턴으로 찾을 수 없습니다.
#X-: Very short
#X-Plane is behind schedule: two weeks
import re

handle=open('mbox-short.txt')
for line in handle:
    line=ine.rstrip()
    if re.search('^From:',line):
        print(line)
       # 탐욕적인 방식 테스트
x = 'My 2 favorite numbers are 19 and 42'
re.findall('\d.*\d',x)
#['2 favorite numbers are 19 and 42']
re.findall('\d.*?\d',x)
#['2 favorite numbers are 1', '9 and 4'
import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x)
print(y)

# ['2', '19', '42']