import socket
from datetime import datetime

server = socket.socket()

server.bind(('localhost', 3030)) # Привязываем серверный сокет к localhost и 3030 порту.
server.listen(5) # Начинаем прослушивать входящие соединения.

print("Start")
while True:
    conn, _ = server.accept()
    data = conn.recv(1024) # Получаем данные из сокета.
    print(data.decode('utf-8'))
    message = datetime.now().strftime("%H:%M:%S")  # отправляем текущее время
    conn.send(message.encode())      # отправляем сообщение клиенту
    conn.close()                     # закрываем подключение