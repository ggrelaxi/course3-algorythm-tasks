def MaximumDiscount(N, price):
    change = True

    while change == True:
        change = False

        for i in range(N - 1, 0, -1):
            try:
                if price[i] > price[i - 1]:
                    temp = price[i]
                    price[i] = price[i - 1]
                    price[i - 1] = temp
                    change = True
            except IndexError:
                break

    result = []
    counter = 0
    part = []

    for i in range(N):
        part.append(price[i])
        counter += 1

        if counter == 3:
            result.append(part)
            part = []
            counter = 0
        elif i == (N-1) and counter != 3:
            result.append(part)

    discount = 0

    for i in range(len(result)):
        try:
            discount += result[i][2]
        except IndexError:
            break

    return discount