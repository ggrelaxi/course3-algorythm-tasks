def SumOfThe(N, data):
    for i in range(N):
        actual = data[i]
        summ = 0
        for j in range(0, N):
            if j == i:
                continue
            summ += data[j]
        if actual == summ:
            return summ