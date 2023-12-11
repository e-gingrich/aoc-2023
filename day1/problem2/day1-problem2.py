import re
from collections import OrderedDict

valid_values_strs = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
valid_values_ints = [1,2,3,4,5,6,7,8,9]


def get_num_val_of_str(num_str):
    for i, n in enumerate(valid_values_strs):
        if (n == num_str):
            return i+1

with open('day1-problem1-input.txt') as f:
    contents = f.read()

    indv_strs = contents.split()
    
    sum = 0
    for indv_str in indv_strs:
        digits_indexes = {}
        c_counter = 1
        str_builder = ""

        for valid_values_str in valid_values_strs:
            if (valid_values_str in indv_str):
                for m in re.finditer(valid_values_str, indv_str):
                    #print (valid_values_str + " found at " + str(m.start()))
                    digits_indexes[m.start()] = get_num_val_of_str(valid_values_str)
                    #print(valid_values_str + ": " + str(indv_str.index(valid_values_str)))

        for i, c in enumerate(indv_str):
            if (c.isdigit()):
                digits_indexes[i] = c
               # print(c + ": " + str(i))

        sorted_di = OrderedDict(sorted(digits_indexes.items()))
        #print (indv_str + ": " + str(sorted_di) + "\n")
        
        first = sorted_di[list(sorted_di.keys())[0]]
        last = sorted_di[list(sorted_di.keys())[len(sorted_di)-1]]
        #print (indv_str + ": " + str(first) + str(last) + "\n")

        indv_sum = (int(first) * 10) + int(last)
        #print (indv_str + ": " + str(indv_sum))
        
        sum += indv_sum

    print (sum)
