def hamming_distance(strand1, strand2):
    ''' 
    input: two str of equal length, representing DNA strands
    output: number of differences between the strands (int)
    '''
    if len(strand1) == len(strand2):
        if type(strand1) and type(strand2) is str:
            if strand1 and strand2:
                
                counter = 0
                for i in range(len(strand1)):
                    if strand1[i]!= strand2[i]:
                        counter +=1
                return counter
    else:
        raise ValueError("Please enter two strings of equal length to represent DNA strands")


#Clarifying Q's:
# - What output should this function give if in cases of invalid input (ie- lengths of input DNA strands are not the same?; input not string?)
# - Do we want this function to be case sensitive?
# - Is there a max or min length of DNA strands for this function?
# - Do we check for whether the string only contains expected DNA sequence data (ie- C,G,A,and T?)
# - What to do in case of an empty strings?

#Pseudocode:
# Handle invalid input:  Check that two parameters are strings of equal length, else raise an Error.  In case of empty strings, return 0.
# - Given valid input: 
# 1- initiate a counter = 0 to keep track of differences
# 2-iterate through each index of string1, comparing the value to that same index in string2.  Add +1 to the counter for each difference found.
# 3- Return the counter (as an int) as the output of the function 