
def missing_k_num(array, k):
    for item in array:
        if not type(item) == int:
            # return "List should have integers only"
            raise ValueError("List should have integers only")
        if item < 1 or item > 1000:
            # return "All list items should be integers greater than zero and less than 1000."
            raise ValueError("All list items should be integers greater than zero and less than 1000.")
    
    if k > (1000 - len(array)):
        raise ValueError(f"there are not {k} missing numbers")
    
    if array == []:
        return k

    prior_num = 0
    for num in array: 
        if num != prior_num +1:    
            missed_nums = num - (prior_num+1)
            if k <= missed_nums:
                return prior_num + k
            else :
                k -= missed_nums
        prior_num = num

    # if iterate through end of list and k has value:
    return array[-1] + k
        
print(missing_k_num([1,3,4,5,7,12],2)) # 6