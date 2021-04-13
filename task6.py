def PatternUnlock(N, hits):
    result = 0
    hypo = 1.4142135623730951
    matrix = [[6,1,9], [5,2,8], [4,3,7]]


    #матрица
    for i in range(len(matrix)):
        print(matrix[i])

    #координаты текущей точки
    def getCords(value):
        cords = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == value:
                    cords.append(i)
                    cords.append(j)
                    break
        return cords

    def getNeighbors(cords):
        x, y = cords
        lineNeighbors = []
        lineNeighbors.append([x, y + 1])
        lineNeighbors.append([x, y - 1])
        lineNeighbors.append([x - 1, y])
        lineNeighbors.append([x + 1, y])

        return [lineNeighbors]


    for i in range(N - 1):
        actualCords = getCords(hits[i])
        nextCords = getCords(hits[i + 1])
        line = getNeighbors(actualCords)

        if (nextCords in line):
            result += 1
        else:
            result += hypo
    
    data = list(str(int(round(result, 5) * 100000)))
    return "".join([num for num in data if num != 0])