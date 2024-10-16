import random
count = int(input())

lista = [int(random.random() * 100) for i in range(0, count)]

temp = set(lista)

lista = list(temp)
print(lista)