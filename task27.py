import copy

def Football(F, N):
    for i in range(1, 3):
        tempArr = copy.copy(F)
        change = True

        while change == True:
            change = False
            for j in range(N - 1):
                current = tempArr[j]

                if current > tempArr[j + 1]:
                    temp = current
                    tempArr[j] = tempArr[j + 1]
                    tempArr[j + 1] = temp
                    change = True
    

        if i == 1:
            temp1 = copy.copy(F)
            temp1.reverse()
            
            if temp1 == tempArr:
                return True

        if i == 2:
            temp2 = copy.copy(F)

            for y in range(N - 1):
                for x in range(y + 1, N):
                    current = temp2[y]
                    next = temp2[x]
                    temp2[y] = next
                    temp2[x] = current

                    if temp2 == tempArr:
                        return True
                    else:
                        temp2 = copy.copy(F)
    return False