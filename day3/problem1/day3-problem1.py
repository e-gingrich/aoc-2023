with open('day3-problem1-input.txt') as f:
    array2D = []
    # loading into a 2d array for easier access
    for line in f.readlines():
        indv_line = []
        for c in line:
            indv_line.append(c)
        array2D.append(indv_line)
    
    
    
