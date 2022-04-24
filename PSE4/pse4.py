def is_palindrome(word):
    '''
    input: string
    output: True if palindrome; False if not
    '''
    if not type(word) == str:
        return ValueError
    
    else:
        n = len(word)
        word = word.lower()
        
        front_index = 0
        
        for i in range(int(n/2)):
            if word[front_index] == word[n-1]:
                front_index += 1
                n -= 1
            else:
                return False
        return True


  # using int() after dividing length by 2 essentially rounds down as 
        # 2.5 will become 2. This avoids attempting to compare the center-most 
        # character of a string that has an odd-numbered length