def MassVote(N, Votes):
    sumVotes = 0
    maxVotes = Votes[0]
    winnerIndex = 1

    for i in range(N):
        sumVotes += Votes[i]
        try:
            nextCandidatVotes = Votes[i + 1]
            if nextCandidatVotes > maxVotes:
                maxVotes = nextCandidatVotes
                winnerIndex += i + 1
        except IndexError:
            break
    
    WinnerCount = 0
    middleVotesValue = sumVotes * 0.5

    for i in range(N):
        if Votes[i] == maxVotes:
            WinnerCount += 1
    
    if WinnerCount > 1:
        return "no winner"
    elif WinnerCount == 1:
        if maxVotes > middleVotesValue:
            return "majority winner " + str(winnerIndex)
        elif maxVotes <= middleVotesValue:
            return "minority winner " + str(winnerIndex)