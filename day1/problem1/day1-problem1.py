with open('day1-problem1-input.txt') as f:
    contents = f.read()

    indv_strs = contents.split()
    
    sum = 0
    for indv_str in indv_strs:
        digits = []
        for i, c in enumerate(indv_str):
            if (c.isdigit()):
                digits.append(int(c))

        #print (digits)
        first = digits[0]
        last = digits[len(digits)-1]
        indv_sum = (first * 10) + last
        print (indv_sum)
        sum += indv_sum

    print (sum)   