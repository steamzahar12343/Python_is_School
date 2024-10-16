list = ["list", "goida", "zov"]
i = 0

while i < len(list):
    print(f'{i} - {list[i]}')
    i += 1
print("----------------------------")

Index = int(input())

if(Index >= len(list) or Index < 0):
    print("Элемента с таким индексом не существует")
else:
    print(list[Index])