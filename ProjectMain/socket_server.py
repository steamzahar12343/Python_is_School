#!/usr/bin/python3.5
from  socket import *
import subprocess, time

# Sever
sock=socket(AF_INET,SOCK_STREAM)
sock.bind(('192.168.0.110',3030))
sock.listen(1)

while True:
    conn, addr = sock.accept()
    print ('Server connect by ',addr)
    while True:

        try:
            data=conn.recv(1024)
        except:
            break
        if not data:
            break
      
        result=subprocess.run(['cmd.exe'], stdout=subprocess.PIPE,stderr=subprocess.PIPE, input=data)
        conn.send(result.stdout) 
        conn.send(result.stderr)
# Интересный момент, может кто знает, у меня так нормальна не заработало, если conn.close() вынести с тела второго цикла.
# В примерах у того же Лутца, соединения закрывают в теле первого цикла. Ладно буду розбератся
        conn.close()