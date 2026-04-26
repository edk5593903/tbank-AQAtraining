figures = [1, 3, 3, 2, 5, 2, 1, 3, 1]               # initial list to be processed
          
counts = {}                                         # setting the empty dic to be filled

for figure in figures:                              # cycle to sort out repeatitions here the counts
    counts[figure] = counts.get(figure, 0) + 1      # recall each figure to sort it out using .get method

max_counts = max(counts.values())                   # to find the max counts' value using .value method

result = None                                       # to declare the result template
for k, v in counts.items():                   # cycle to find among dic any/all proper pairs using .items
    if v == max_counts:                         # the sign for the proper pairs
        result = k                                # to give the result meaning of the key according upper the sign
        break                                       # to stop the cycle with the first result (any one)
    
print(result)                                       # to output the key