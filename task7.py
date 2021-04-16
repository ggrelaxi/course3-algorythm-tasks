def WordSearch(length, string, sub):
    splitStr = string.split(" ")
    stringWithoutBigWords = []
    for i in range(len(splitStr)):
        if len(splitStr[i]) > length:
            subStr = ""
            for j in range(len(splitStr[i])):
                if (j + 1) % length == 0 and j > 0:
                    subStr += splitStr[i][j] + " "
                else:
                    subStr += splitStr[i][j]
            stringWithoutBigWords.append(subStr)
        else:
            stringWithoutBigWords.append(splitStr[i])

    actualStr = " ".join(stringWithoutBigWords).split(" ")
    resultStr = []
    resultCount = []
    index = 0

    for i in range(len(actualStr)):
        subStr = ""

        if len(actualStr[i]) == length:
            resultStr.append(actualStr[i])
            index = i + 1
        elif i == index:
            subStr = actualStr[i]
            if i + 1 == len(actualStr):
                resultStr.append(subStr)
            for j in range(i + 1, len(actualStr)):
                if len(subStr + " " + actualStr[j]) > length:
                    resultStr.append(subStr)
                    index = j
                    break
                else:
                    subStr += " " + actualStr[j]

    for i in range(len(resultStr)):
        subStr = resultStr[i]
        word = subStr.split(" ")
        if sub in word:
            resultCount.append(1)
        else:
            resultCount.append(0)

    return resultCount