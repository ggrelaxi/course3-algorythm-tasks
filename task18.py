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

    while result == False:
        startSlice = random.randint(0,endOfRange)
        changePart = tempArray[startSlice:startSlice+3]

        sortSlice = sorting(changePart)

        for i in range(3):
            indexOne, indexTwo, indexThree = changePart

            if changePart == sortSlice:
                break
            else:
                changePart[i] = indexTwo
                changePart[i+1] = indexThree
                changePart[i+2] = indexOne

        tempArray[startSlice] = indexOne
        tempArray[startSlice+1] = indexTwo
        tempArray[startSlice+2] = indexThree

        if tempArray == sortArray:
            result = True
            break

    return result