from  socket import *

while True:
    sock=socket(AF_INET,SOCK_STREAM)
# если не на одной машине будите тестить localhost заменить на IP машины где будет сервер запущен
    sock.connect(('192.168.0.110',3030))
    sinst=input ("введите команду: ")
    if sinst=='exit1':
        break
    st=''
    for i in sinst:
      
        if i != "~":
            st=st+i
        else:
            st=st+'\n'
    # Для cmd переход на новую строку - выполнения команды      
    sinst=st+"\n"  
    sinst=sinst.encode('cp866')
    # Метод socket.send ожидает последовательность байтов, а не строку. (методом str.encode)
    sock.send(sinst)
   
    while True:
        try:
            data=sock.recv(1024)
        except:
            break 
        if not data:
            break
        print(data.decode('cp866'))
    sock.close()