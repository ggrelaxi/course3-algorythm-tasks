def SherlockValidString(s):
    symbolsCount = []
    symbols = []
    length = len(s)

    for x in range(length):
        symbol = s[x]
        if symbol not in symbols:
            symbols.append(symbol)
            symbolsCount.append([symbol, 1])
        else:
            for j in range(len(symbolsCount)):
                tempSymbol, count = symbolsCount[j]
                if symbol == tempSymbol:
                    symbolsCount[j][1] = count + 1

    valid = True
    char, counter = symbolsCount[0]

    for m in range(1, len(symbolsCount)):
        tempChar, tempCounter = symbolsCount[m]
        if counter != tempCounter:
            valid = False
            break

    if valid == True:
        return valid

    symbols = []
    symbolsCount = []

    for i in range(length):
        tempStr = s[0:i] + s[i+1:length]
        
        for x in range(length - 1):
            symbol = tempStr[x]
            if symbol not in symbols:
                symbols.append(symbol)
                symbolsCount.append([symbol, 1])
            else:
                for j in range(len(symbolsCount)):
                    tempSymbol, count = symbolsCount[j]
                    if symbol == tempSymbol:
                        symbolsCount[j][1] = count + 1

        valid = True
        char, counter = symbolsCount[0]
        
        for m in range(1, len(symbolsCount)):
            tempChar, tempCounter = symbolsCount[m]
            if counter != tempCounter:
                valid = False
                break

        if valid == True:
            return valid

        symbols = []
        symbolsCount = []

print(SherlockValidString("xxyyzzzz"))
