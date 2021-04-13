def PatternUnlock(N, hits):
    result = 0
    for i in range(N):
        result += hits[i]

    data = list(str(result))

    for i in range(len(data)):
        if data[i] == 0:
            del data[i]
    
    return "".join(data)