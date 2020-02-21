#프로토콜(TCP)#파이썬 으로 간단한 웹사이트만들기
import socket #임폴트소켓


mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# 소켓 핸들링 생성
mysock.connect( ('data.pr4e.org', 80) ) #소켓 연결
cmd='GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()#\n 은 줄을 건너뛴다 소켓에 보낼 문자열 준비 + 전송을 위한 encode. unicode -> UTF-8
mysock.send(cmd)#문자열 전송


while True:
    data=mysock.recv(512)##socket.recv : Receive data from the socket. 512는 버퍼의 크기(512단위로 받아옴)
    if (len(data) < 1): #데이터 가 끝나면 을 의미한다 
        break
    print(data.decode(),end='')# #통신을 위해 encode된 데이터를 decode해서 print. UTF-8 -> unicode
mysock.close()