def BigMinus(s1, s2):
    list1 = list(s1)
    list2 = list(s2)

    biggest = []
    smallest = []
    if s1 == s2:
        return "0"
    if len(s1) >= len(s2) and len(s1) > 1:
        biggest = list1
        smallest = list2
    elif len(s1) == len(s2) and len(s1) == 1:
        minuend = int(list1[0])
        subtrahend = int(list2[0])
        if minuend >= subtrahend:
            result = minuend - subtrahend
            return str(result)
        elif minuend < subtrahend:
            result = (subtrahend - minuend)
            return str(result)
    else:
        biggest = list2
        smallest = list1

    biggest.reverse()
    smallest.reverse()
    
    result = []

    for i in range(len(biggest)):
        try:
            minuend = int(biggest[i])
            subtrahend = int(smallest[i])
            if minuend >= subtrahend:
                actualNum = minuend - subtrahend
                result.append(str(actualNum))
            elif subtrahend > minuend:
                for i in range(i + 1, len(biggest)):
                    if int(biggest[i]) != 0:
                        num = int(biggest[i])
                        resultNum = num - 1
                        biggest[i] = str(resultNum)
                        break
                    elif int(biggest[i]) == 0:
                        biggest[i] = "9"
                        continue
                minuend += 10
                actualNum = minuend - subtrahend
                result.append(str(actualNum))
        except IndexError:
            result.append(biggest[i])

    result.reverse()
    resultStr =  "".join(result)

    return resultStr