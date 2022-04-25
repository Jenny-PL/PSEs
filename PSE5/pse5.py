import copy 

def pairs_with_given_sum(list, target_sum):
# list = [97,51,49,35,3,65]
    if type(target_sum) != int:
        return TypeError("Please give an integer value for target sum ")

    for num in list:
        if type(num) != int:
            return TypeError("Please give a list of integers")

    list_to_alter = list.copy()
    num_of_pairs = 0

    for num in list:
        first_num = num
        list_to_alter.remove(first_num)
        for item in list_to_alter:
            sum = first_num + item
            if sum == target_sum:
                num_of_pairs += 1
    return num_of_pairs

result = pairs_with_given_sum([], 100)
print(result)

# Time complexity?
# O(n + n2) where n is the length of the list.  
# Because I chose to go through the entire list to check if the values
#  within it were integers, this added the O(n) to the 
# nested loop, which is (O)n**2.



#Space complexity?
# O(n), where n is the length of the list. I made a copy of the list, 
# so this would take up 2*O(n), and added a few other variables:
#  sum, num_of_pairs, which I believe would make it 2*O(n) + 2 (??), 
# however with dropping the constants, I believe it is an O(n) space complexity.