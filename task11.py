def BigMinus(s1, s2):
    num1 = int(s1)
    num2 = int(s2)
    difference  = num1 - num2

    if difference < 0:
        difference = difference * (-1)

    return str(difference)