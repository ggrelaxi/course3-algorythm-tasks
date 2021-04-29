import random
import time

def MisterRobot(N, data):
    start_time = time.time()
    tempArray = data.copy()

    def sorting(arr):
        change = True
        
        while change == True:
            change = False

            for i in range(len(arr)):
                try:
                    if arr[i] > arr[i + 1]:
                        temp = arr[i]
                        arr[i] = arr[i + 1]
                        arr[i + 1] = temp
                        change = True
                except IndexError:
                    break
        
        return arr

    sortArray = sorting(data)

    result = False

    endOfRange = N - 3

    while (int(time.time() - start_time) < 1):
        startSlice = random.randint(0, endOfRange)
        changePart = tempArray[startSlice:startSlice+3]
        indexOne, indexTwo, indexThree = changePart

        tempArray[startSlice] = indexTwo
        tempArray[startSlice+1] = indexThree
        tempArray[startSlice+2] = indexOne

        if tempArray == sortArray:
            result = True
            break

    return result