def cycles(arr):
        result = []
        for i in range((len(arr) - 1) + 1):
            for j in range((len(arr) - i - 1) + 1):
                k = i + j
                max = arr[j]
                
                for m in range(j, k + 1):
                    if arr[m] > max:
                        max = arr[m]
                
                result.append(max)
        print(result)
        return result

def TransformTransform(A, N):
    first = cycles(A)
    second = cycles(first)

    sum = 0
    for i in range(len(second)):
        sum += second[i]

    return sum % 2 == 0