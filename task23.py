def TreeOfLife(H, W, N, tree):
    result = []

    for a in range(len(tree)):
        tempString = list(tree[a])
        temp = []
        for b in range(len(tempString)):
            char = tempString[b]
            if char == ".":
                temp.append([0,0])
            else:
                temp.append([1,1])
        result.append(temp)

    for c in range(N):
        if c % 2 == 0:
            for d in range(len(result)):
                tempString = result[d]
                for m in range(len(tempString)):
                    result[d][m][1] += 1
                    if result[d][m][0] == 0:
                        result[d][m][0] = 1

        else:
            for e in range(len(result)):
                tempString = result[e]
                for f in range(len(tempString)):
                    result[e][f][1] += 1
                    if result[e][f][0] == 0:
                        result[e][f][0] = 1    

            deleteCords = []

            for h in range(len(result)):
                line = result[h]
                for g in range(len(line)):
                    pointState, pointAge = line[g]
                    if pointAge >= 3:
                        if h - 1 >= 0:
                            top = [h - 1, g]
                            deleteCords.append(top)
                        if h + 1 <= W:
                            bottom = [h + 1, g]
                            deleteCords.append(bottom)
                        if g - 1 >= 0:    
                            left = [h, g - 1]
                            deleteCords.append(left)
                        if g + 1 <= H:    
                            right = [h, g + 1]
                            deleteCords.append(right)
                        deleteCords.append([h,g])

            for n in range(len(deleteCords)):
                wid, he = deleteCords[n]
                
                try:
                    result[wid][he][0] = 0
                    result[wid][he][1] = 0
                    
                except IndexError:
                    continue

    resultArr = []

    for p in range(len(result)):
        tempString = result[p]
        temp = ""
        for r in range(len(tempString)):
            char = tempString[r][1]
            if char == 0:
                temp += "."
            else:
                temp += "+"
        resultArr.append(temp)

    return resultArr