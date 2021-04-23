def UFO(N, data, octal):
    result = []
    
    for i in range(N):
        actualNumToStr = str(data[i])
        actualNumToStrLen = len(actualNumToStr)
        sum = 0

        for j in range (len(actualNumToStr)):
            actualNum = int(actualNumToStr[j])
            actualStage = actualNumToStrLen - j - 1
            actualEightStage = 0

            if octal == True:
                actualEightStage = 8 ** actualStage
            else:
                actualEightStage = 16 ** actualStage
                
            sum += actualNum * actualEightStage
            
        result.append(sum)
    
    return result