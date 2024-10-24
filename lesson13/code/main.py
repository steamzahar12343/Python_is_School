PI = 3.141592


def S(rad: float) -> float:
    Sup = PI * rad * rad 
    return Sup

rad = float(input())
print(S(rad))