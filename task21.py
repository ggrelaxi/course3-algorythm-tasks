import random

def BiggerGreater(input):
    words = []
    length = len(input)
    factorial = 1
    
    for i in range(1, length + 1):
        factorial *= i
    resultWord = input

    symbolsCount = []
    symbols = []
    for i in range(length):
        symbol = input[i]
        if symbol not in symbols:
            symbols.append(symbol)
            symbolsCount.append([symbol, 1])
        else:
            for j in range(len(symbolsCount)):
                tempSymbol, count = symbolsCount[j]
                if symbol == tempSymbol:
                    symbolsCount[j][1] = count + 1
        
    doubleSymbolArr = []

    for i in range(len(symbolsCount)):
        tempSymbol, count = symbolsCount[i]
        if count > 1:
            doubleSymbolArr.append(symbolsCount[i])

    factorialComposition = 1    
    for i in range(len(doubleSymbolArr)):
        tempSymbol, count = doubleSymbolArr[i]
        tempFactorial = 1
        for j in range(1, count + 1):
            tempFactorial *= j
        
        factorialComposition *= tempFactorial

    totalWords = factorial // factorialComposition

    while len(words) < totalWords:
        firstIndex = random.randint(0, length - 1)
        secondIndex = random.randint(0, length - 1)

        temp = list(resultWord)

        firstSymbol = temp[firstIndex]
        secondSymbol = temp[secondIndex]

        temp[firstIndex] = secondSymbol
        temp[secondIndex] = firstSymbol

        tempResult = "".join(temp)

        if tempResult not in words:
            words.append(tempResult)
        
        resultWord = tempResult

    bigWords = []
    for i in range(len(words)):
        if words[i] > input:
            bigWords.append(words[i])

    change = True

    while change == True:
        change = False

        for i in range(len(bigWords) - 1):
            firstWord = bigWords[i]
            secondWord = bigWords[i + 1]

            if firstWord > secondWord:
                tempWord = firstWord
                bigWords[i] = secondWord
                bigWords[i + 1] = tempWord
                change = True

    try:
        minLeksikoWord = bigWords[0]
        if minLeksikoWord > input:
            return minLeksikoWord
        else:
            return ""
    except:
        return ""