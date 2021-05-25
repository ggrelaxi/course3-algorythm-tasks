def BalancedParentheses(N):
    result = []

    def balance(search, left, right, pairs):
        if left == pairs and right == pairs:
            result.append(search)
        else:
            if left < pairs:
                balance(search + "(", left + 1, right, pairs)
            if right < left:
                balance(search + ")", left, right + 1, pairs)
    balance('', 0, 0, N)
    
    parse = " ".join(result)

    return parse