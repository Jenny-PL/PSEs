def hamming_distance(strand1, strand2):
    if len(strand1) == len(strand2):
        if type(strand1) and type(strand2) is str:
            if strand1 and strand2:
                
                counter = 0
                strand1 = [letter for letter in strand1]
                strand2 = [letter for letter in strand2]
                    
                for i in range(len(strand1)):
                    if strand1[i] != strand2[i]:
                        counter +=1
                return counter
    else:
        raise ValueError("Please enter two strings of equal length to represent DNA strands")
        