def squirrel(N):
    factorial = 1

    for i in range(2, N + 1):
        factorial *= i

    return int(str(factorial)[0])
