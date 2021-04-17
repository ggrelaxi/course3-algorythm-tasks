import math
from unittest.loader import findTestCases

def TheRabbitsFoot(s, encode):
    if encode == True:
        withoutSpaces = "".join(s.split(" "))
        length = len(withoutSpaces)
        min = math.floor(length ** 0.5)
        max = math.ceil(length ** 0.5)

        fitAsMatrix = False

        while fitAsMatrix == False:
            if length < min * max:
                fitAsMatrix = True
            else:
                min += 1

        matrix = []
        count = 0
        for i in range(min):
            horizontal = []
            for j in range(max):  
                horizontal.append(withoutSpaces[count])
                count += 1
                if count == length:
                    break;
            matrix.append(horizontal)

        result = ""

        for i in range (min):
            word = ""
            for j in range(max):
                try:
                    word += matrix[j][i]
                except IndexError:
                    break
            if i < max:
                word += " "
            result += word
        
        return result

    else:
        split = s.split(" ")
        min = 0
        max = len(split)
        for i in range(max):
            if min < len(split[i]):
                min = len(split[i])
        
        print(min, max)

        matrix = []

        for i in range(min):
            for j in range(max):
                try:
                    matrix.append(split[j][i])
                except IndexError:
                    break;

        return "".join(matrix)