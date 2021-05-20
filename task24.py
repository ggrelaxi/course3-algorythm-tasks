Matrix = ["123456", "234567", "345678", "456789"]

def MatrixTurn(Matrix, M, N, T):
    for i in range(T):
        temp = []

        for i in range(M):
            line = Matrix[i]
            arr = list(line)
            temp.append(arr)

        
        top = 0
        bottom = len(temp) - 1
        left = 0
        right = len(temp[0]) - 1

        while left < right and top < bottom:
            prev = temp[top+1][left]

            for i in range(left, right + 1):
                current = temp[top][i]
                temp[top][i] = prev
                prev = current
            
            top += 1

            for i in range(top, bottom+1):
                current = temp[i][right]
                temp[i][right] = prev
                prev = current
            
            right -= 1

            for i in range (right, left-1, -1):
                current = temp[bottom][i]
                temp[bottom][i] = prev
                prev = current

            bottom -= 1

            for i in range(bottom, top-1, -1):
                current = temp[i][left]
                temp[i][left] = prev
                prev = current

            left += 1

        result = []
        
        for i in range(len(temp)):
            line = "".join(temp[i])
            result.append(line)

        Matrix = result

    return Matrix