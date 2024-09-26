import socket
Socket = socket.socket()

Socket.connect(('localhost', 3030)) # Подключаемся к нашему серверу.
Socket.send('Hello, Habr!'.encode('utf-8')) # Отправляем фразу.
data = Socket.recv(1024) #Получаем данные из сокета.
print(data.decode())
Socket.close()