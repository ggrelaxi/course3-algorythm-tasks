def SynchronizingTables(N, ids, salary):
    result = [0 for i in range(N)]
    sortedIDS = sorted(ids)
    sortedSalary = sorted(salary)
    equal = []
    for i in range(N):
        equal.append([sortedIDS[i], sortedSalary[i]])
    
    for i in range(N):
        [id, sal] = equal[i]
        correctID = ids.index(id)
        result[correctID] = sal
    
    return result