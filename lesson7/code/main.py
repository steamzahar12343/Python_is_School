sum = 0
isSum = True

while isSum:
    Input = input()
    match Input:
        case "sum":
            print("Сумма равна: ", sum)
            sum = 0
        case "exit":
            isSum = False
        case "quit":
            isSum = False
        case _:
            sum += int(Input)
