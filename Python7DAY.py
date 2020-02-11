#파일열기,파일읽기 
fl=open('mbox-short.txt.txt')
print(fl)
count=0
for line in fl:
    count=count+1
    a=line.rstrip()
print(a)
print(count)
print(a.upper())
