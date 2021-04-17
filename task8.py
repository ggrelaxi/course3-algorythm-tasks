def SumOfThe(N, data):
    for i in range(N):
        actual = data[i]
        summ = 0
        for j in range(i, N):
            summ += data[j]
        if actual == summ:
            return summ
      



SumOfThe(7, [100, -50, 10, -25, 90, -35, 90])