def Unmanned(L, N, track):
    def getlightsRange(time, lights):
        distance, redTime, greenTime = lights
        actualLight = "red"

        timeline = []
        result = []
        
        actualRange = redTime
        count = 1

        for i in range(time):
            timeline.append(i)

        light = []

        for i in range(len(timeline)):
            light.append(i + 1)

            if count < actualRange and i < (len(timeline) - 1):
                count += 1
            elif i == (len(timeline) - 1):
                lists = [light, actualLight]
                result.append(lists)
            else:
                lists = [light, actualLight]
                result.append(lists)
                light = []
                count = 1
                if actualLight == "red":
                    actualLight = "green"
                else:
                    actualLight = "red"
        
        return result
    
    time = track[0][0]

    if L < time:
        return L

    totalDistance = L

    for i in range(N):
        distance, redTime, greenTime = track[i]
    
        lightsRange = getlightsRange(time, track[i])
       
        actualColor = ""
        timeIndex = 0

        for i in range(len(lightsRange)):
            listRange, color = lightsRange[i]
            if time in listRange:
                timeIndex = listRange.index(time) + 1
                actualColor = color

        if actualColor == "red":
            timeLosses = redTime - timeIndex
            totalDistance += timeLosses
            time += distance + timeLosses

    return totalDistance