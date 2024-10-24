lenBoard = int(input())
lenGub = int(input())

LENGTH = 0

stroke = ""

SBoard = lenBoard * lenBoard
SGub = lenGub * lenGub

CountTiles = int(SBoard / SGub)

ColorTiles = []

for x in range(lenBoard):
    for y in range(lenBoard):
        temp = False        
        for i in ColorTiles:
            if(i == [[x,y]]):
                temp = True
                break
            else:
                temp = False
                break
            
        if(temp):
            continue
        else:
            ColorTiles += [[x,y]]
            LENGTH += 1

print(LENGTH)