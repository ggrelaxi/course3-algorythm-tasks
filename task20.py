resultStr = ""
operationsAdd = []
operationsDelete = []
lastOperationId = 0

def BastShoe(command):
    global resultStr
    global operationsAdd
    global operationsDelete
    global lastOperationId

    if len(command) == 1:
        operationNumber = int(command)
    else:
        operationNumber = int(command[0])
        subString = command[2:]
    
    if operationNumber == 1:
        if lastOperationId == 4:
            operationsAdd = []
            operationsDelete = []

        result = resultStr + subString
        operationsAdd.append([resultStr, result, 1])

        resultStr = result

        lastOperationId = 1
        return result

    elif operationNumber == 2:
        if lastOperationId == 4:
            operationsAdd = []
            operationsDelete = []
        if len(resultStr) <= int(subString):
            result = ""
            operationsAdd.append([resultStr, result, 2])
            resultStr = ""

            return resultStr
        else:
            result = resultStr[0:(len(resultStr) - int(subString))]
            operationsAdd.append([resultStr, result, 2])
            resultStr = result

            return resultStr            
        
    elif operationNumber == 3:
        if (len(resultStr) - 1) < int(subString):
            resultStr = ""
            return resultStr
        else:
            symbol = resultStr[int(subString)]
            resultStr = symbol
            return resultStr
    
    elif operationNumber == 4:
        lastOperationId = 4

        if len(operationsAdd) == 0:
            return resultStr

        else:
            lastOperation = operationsAdd.pop()
            before, after, operationId = lastOperation

            operationsDelete.append([after, before, 4])
            resultStr = before

            return resultStr

    elif operationNumber == 5:
        lastOperationId = 5
        if len(operationsDelete) == 0:
            return resultStr
        elif len(operationsDelete) == 1:
            before, after, operationId = operationsDelete[0]
            resultStr = before
            operationsDelete.pop()
            operationsAdd.append([after, before, 1])
            return resultStr
        else:
            before, after, taskId = operationsDelete[(len(operationsDelete) - 1)]
            resultStr = before
            operationsDelete.pop()
            operationsAdd.append([after, before, 1])
            return resultStr

    return resultStr