mydict = dict(Name = 'Без имени', Age = -1)
ThisName = input()
ThisAge = int(input())
mydict['Name'] = ThisName
mydict['Age'] = ThisAge

for key in mydict:
    print(f'{key} = {mydict[key]}')