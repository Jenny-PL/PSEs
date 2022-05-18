# Handle invalid input: 
#  -- If item in list is not type(int), is not > 0, or is not < 1001, then raise ValueError

# Logic:
# --  if k > (1000 minus length of the list ). example: 2 missing numbers, k =4, then return ValueError "there are not {k} missing numbers in this list"
# -- Plan:
# -- Dictionary Solution? 
#   -- Make a dictionary where key= index and value = number, if the full, complete list was given (1 to 1000, inclusive): (0,1,2,3...999)
# -- Example: {0:1, 1:2, 2:3, ....999:1000}
# -- initialize a variable to count missing numbers, set equal to zero.
# -- initialize a key variable, set equal to i ?
#    -- Iterate through given list; if list[i] is not equal to dictionary[key=i] (example i=0, dictionary[0], where given list= [4,6,8], k=3) then add 1 to missing number variable
#  --  increment key +1.
#   -- next check if list[i] is equal to dict[incremented_key]; if it is not, add 1 to missing variable number.  (Make this a while loop; while list[i] != dict[key]
#  -- Once missing_number == k: return dictionary[key] for that index.

def missing_k_num(array, k):
    for item in array:
        if not type(item) == int:
            raise ValueError("List should have integers only")
        if item < 1 or item > 1000:
            raise ValueError("All list items should be integers greater than zero and less than 1000.")
    
    if k > (1000 - len(array)):
        return f"there are not {k} missing numbers"
    
    if array == []:
        return k
    
    # making dictionary with list_index:value for a list with values from 1 -->1000
    dict_of_integers = {}
    for i in range(0,1001):
        dict_of_integers[i] = i+1
    
    key = 0
    for i in range(len(array)):  
        while array[i] != dict_of_integers[key]:
            k -= 1
            if k == 0:
                return dict_of_integers[key]
            key += 1
        if array[i] == dict_of_integers[key]:
            key += 1
    # if get through whole list, and k is not zero... return last item in list + k
    return (k+array[-1])
        
print(missing_k_num([1,3,4,5,7],2)) # 6
print(missing_k_num([1,3,4,5,7],12)) # 17  array[-1]= 7, k=10

    
    





    