def Keymaker(K):
    doors = []

    for i in range(K):
        doors.append(False)

    for i in range(0, K):
        if i == 0:
            for j in range(K):
                doors[j] = True

        elif i == 1:
            for m in range(1, K, 2):
                doors[m] = False

        elif i == 2:
            for y in range(2, K, 3):
                value = doors[y]
                if value == True:
                    doors[y] = False
                else:
                    doors[y] = True

        else:
            for x in range(i, K, i):            
                nextvalue = doors[i]

                if nextvalue == True:
                    doors[i] == False
                else:
                    doors[i] == True
        
    result = ""

    for z in range(K):
        if doors[z] == True:
            result += "1"
        else:
            result += "0"

    return result