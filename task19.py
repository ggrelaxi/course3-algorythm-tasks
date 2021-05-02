def ShopOLAP(N, items):
    result = []
    resultArrayStr = []
    tempGoods = []

    for i in range(N):
        item, count = items[i].split(" ")

        if item in tempGoods:
            for j in range(len(result)):
                if result[j][0] == item:
                    numCount = int(result[j][1])
                    summ = numCount + int(count)
                    result[j][1] = str(summ)
        else:
            tempGoods.append(item)
            result.append([item, count])

    change = True
    
    while change == True:
        change = False
        for i in range(len(result) - 1):
            item, count = result[i]
            nextItem, nextCount = result[i + 1]
            
            if int(count) < int(nextCount):
                result[i][0] = nextItem
                result[i][1] = nextCount
                result[i+1][0] = item
                result[i+1][1] = count
                change = True

    result.sort()
    
    for i in range(len(result)):
        item = result[i]
        string = " ".join(item)
        resultArrayStr.append(string)

    return resultArrayStr  