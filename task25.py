def TransformTransform(A, N):
    result = []

    for i in range(len(A) - 1):
        for j in range(len(A) - i - 1):
            k = i + j
            
            max = A[j]
            for m in range(k):
                if A[m] > max:
                    max = A[m]
            
            result.append(max)
    
    secondResult = []

    for g in range(len(result) - 1):
        for x in range(len(result) - g - 1):
            k = g + x
            
            max = result[x]
            for q in range(k):
                if result[q] > max:
                    max = result[q]
            
            secondResult.append(max)

    summ = 0
    for y in range(len(secondResult)):
        summ += secondResult[y]

    return summ % 2 == 0
