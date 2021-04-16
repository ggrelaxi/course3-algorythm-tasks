def WordSearch(length, string, sub):
    splitStr = string.split(" ")
    stringWithoutBigWords = []
    for i in range(len(splitStr)):
        if len(splitStr[i]) > 12:
            subStr = ""
            for j in range(len(splitStr[i])):
                if (j + 1) % 12 == 0 and j > 0:
                    subStr += splitStr[i][j] + " "
                else:
                    subStr += splitStr[i][j]
            stringWithoutBigWords.append(subStr)
        else:
            stringWithoutBigWords.append(splitStr[i])

    actualStr = " ".join(stringWithoutBigWords)
    print(actualStr)
    def needWrap(spaceIndex, ind):
        prevWord = string[ind:spaceIndex]
        nextWord = string[spaceIndex+1:].split(" ")[0]
        if len(prevWord) == length:
            return [spaceIndex, True]
        elif len(prevWord) + len(nextWord) + 1 > length:
            return [spaceIndex + 1, True]
        else:
            return [spaceIndex, False]

    resultStr = []
    resultCount = []
    index = 0

    for i in range(len(actualStr)):
        if actualStr[i] == " ":
            result = needWrap(i, index)
            actIndex = result[0]
            isNeedWrap = result[1]
            if isNeedWrap == True:
                subStr = actualStr[index:i]
                resultStr.append(subStr)
                index = actIndex
    splitStr = actualStr.split(" ")
    resultStr.append(splitStr[len(splitStr) - 1])
                    
    for i in range(len(resultStr)):
        subStr = resultStr[i]
        word = subStr.split(" ")
        if sub in word:
            resultCount.append(1)
        else:
            resultCount.append(0)
    
    return resultCount