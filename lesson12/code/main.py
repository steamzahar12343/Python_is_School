def Chet(Value: int) -> bool:
    if(Value % 2 == 0):
        return True  
    else:
        return False  
    
def MaxValue(LS: list) -> int:
    MV = 0
    for i in LS:
        if(i > MV):
            MV = i
    return MV   
    
def SR(*iss: int) -> float:
    sr = 0
    i = 0
    maxi = 0
    for n in iss:
        i +=1
        maxi += n
    sr = maxi / i
    return sr
    
print(Chet(1))
print(Chet(2))
print(MaxValue([31,12,45,4,5]))

print(SR(5,2))