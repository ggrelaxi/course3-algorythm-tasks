def LineAnalysis(line):
    pattern = ""
    
    for i in range(len(line)):
        subStr = line[0:i+1]
        subStrLen = len(subStr)
        nextPart = line[subStrLen:subStrLen+subStrLen]
        if subStr == nextPart or len(subStr) > len(nextPart):
            pattern = subStr
            break

    if len(pattern) == 0:
        return False

    stringIsCorrect = True

    for i in range(0, len(line), len(pattern)):
        try:
            part = line[i:i+len(pattern)]
            if len(part) == len(pattern) and part != pattern:
                stringIsCorrect = False
            elif len(part) != len(pattern):
                break
                
        except IndexError:
            break
        
    return stringIsCorrect