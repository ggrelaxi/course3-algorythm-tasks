def MadMax(N, Tele):
    sort = sorted(Tele)
    centerIndex = (N // 2) - 1

    for i in range(N):
        if i > centerIndex and i < (N - centerIndex):
            first = sort[i]
            last = sort[N - (i - centerIndex)]
            sort[i] = last
            sort[N - (i - centerIndex)] = first

    return sort