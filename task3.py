def ConquestCampaign(N, M, L, battalion):
    days = 0
    victory = False

    #нарисовали карту
    map = []
    for i in range(N):
        line = []
        for j in range(M):
            line.append("bunt")
        map.append(line)
    
    # разобрали координаты на массивы [x, y]
    desantCords = []
    for i in range(len(battalion)):
        singleDesant = []
        if i % 2 == 0:
            singleDesant.append(battalion[i])
            singleDesant.append(battalion[i + 1])
            desantCords.append(singleDesant)
    
    #первая высадка
    for i in range(len(desantCords)):
        x, y = desantCords[i]
        if (x - 1) < N and (y - 1) < M:
            map[x - 1][y - 1] = "win"
    
    days += 1

    #Дальнейший захват
    while victory == False:
        for i in range(len(desantCords)):
            singleDesant = []
            x, y = desantCords[i]
            desantCords.append([x, y + 1])
            desantCords.append([x, y - 1])
            desantCords.append([x - 1, y])
            desantCords.append([x + 1, y])

        for i in range(len(desantCords)):
            x, y = desantCords[i]
            if (x - 1) < N and (y - 1) < M:
                map[x - 1][y - 1] = "win"

        #Если после текущего дня, не осталось клетов с бунтовщиками - победа!!
        for i in range(len(map)):
            victory = True
            for j in range(len(map[i])):
                if map[i][j] == "bunt":
                    victory = False
                    break
                break
            
        days += 1

    return days