def odometer(data):
    result = 0

    for i in range(len(data)):
        if i == 0:
            result += data[i] * data[i + 1]
        elif i % 2 == 0:
            hour = data[i + 1] - data[i - 1]
            result += data[i] * hour
    
    return result