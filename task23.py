def TreeOfLife(H, W, N, tree):
    result = []

    for i in range(len(tree)):
        tempString = list(tree[i])
        temp = []
        for j in range(len(tempString)):
            char = tempString[j]
            if char == ".":
                temp.append([0, 0])
            else:
                temp.append([1,1])
        result.append(temp)        


    for i in range(N):
        if i % 2 == 0:
            for j in range(len(result)):
                tempString = result[j]
                for m in range(len(tempString)):
                    result[j][m][1] += 1
                    if result[j][m][0] == 0:
                        result[j][m][0] = 1

        else:
            for j in range(len(result)):
                tempString = result[j]
                for m in range(len(tempString)):
                    result[j][m][1] += 1
                    if result[j][m][0] == 0:
                        result[j][m][0] = 1    

            deleteCords = []

            for j in range(len(result)):
                line = result[j]
                for m in range(len(line)):
                    pointState, pointAge = line[m]
                    if pointAge >= 3:
                        top = [j - 1, m]
                        deleteCords.append(top)
                        bottom = [j + 1, m]
                        deleteCords.append(bottom)
                        left = [j, m - 1]
                        deleteCords.append(left)
                        right = [j, m + 1]
                        deleteCords.append(right)
                        deleteCords.append([j,m])

            for j in range(len(deleteCords)):
                w, h = deleteCords[j]
                
                try:
                    result[w][h][0] = 0
                    result[w][h][1] = 0
                    
                except IndexError:
                    continue

    resultArr = []
    
    for i in range(len(result)):
        tempString = result[i]
        temp = ""
        for j in range(len(tempString)):
            char = tempString[j][1]
            if char == 0:
                temp += "."
            else:
                temp += "+"
        resultArr.append(temp)

    return resultArr