def formingMagicSquare(s):
    cost = 0
    b1 = [[2, 9, 4], [7, 5, 3], [6, 1, 8]]
    b2 = [[6, 7, 2], [1, 5, 9], [8, 3, 4]]
    b3 = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
    b4 = [[4, 3, 8], [9, 5, 1], [2, 7, 6]]
    b5 = [[8, 3, 4], [1, 5, 9], [6, 7, 2]]
    b6 = [[6, 1, 8], [7, 5, 3], [2, 9, 4]]
    b7 = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
    b8 = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
    baseline = [b1, b2, b3, b4, b5, b6, b7, b8]
    
    for i in range(3):
        for j in range(3):
            cost += abs(s[i][j] - baseline[0][i][j])
    
    for a in baseline[1::]:
        t = 0
        for i in range(3):
            for j in range(3):
                t += abs(s[i][j] - a[i][j])
        if t <= cost:
            cost = t   
    return cost




