import socket
from requests import get
# Определяем имя устройства в сети

hostname = socket.gethostname()

# Определяем локальный (внутри сети) IP-адрес

local_ip = socket.gethostbyname(hostname)

# Определяем глобальный (публичный / в интернете) IP-адрес

public_ip = get('http://api.ipify.org').text