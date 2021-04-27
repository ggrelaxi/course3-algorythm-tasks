def TankRush(H1, W1, S1, H2, W2, S2):
    bigMap = S1.split(" ")
    smallMap = S2.split(" ")

    firstSymbolAtSmallMap = smallMap[0][0]

    result = False

    for i in range(H1):
        for j in range(W1):
            if bigMap[i][j] == firstSymbolAtSmallMap:
                result = True
                for y in range(H2):
                    for x in range(W2):
                        try:
                            actualSymbolAtBigMap = bigMap[i + y][j + x]
                            if actualSymbolAtBigMap != smallMap[y][x]:
                                result = False
                                break
                        except IndexError:
                            result = False
                            break

            if result == True:
                return result

    return result