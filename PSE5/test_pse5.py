from pse5 import pairs_with_given_sum

# example input 1:[97, 51, 49, 35, 3, 65], 100
# expected output 1: 3

# example input 2:[], 50
# expected output 2: 0

def test_nominal_case_find_pairs_to_reach_sum():
    # arrange
    list = [97, 51, 49, 35, 3, 65]
    target_sum = 100
    # act
    result = pairs_with_given_sum(list, target_sum)
    # assert
    assert result == 3
    
def test_find_pairs_to_reach_sum_empty_returns_0():
    # arrange
    list = []
    target_sum = 50
    
    # act
    result = pairs_with_given_sum(list, target_sum)
    # assert
    assert result == 0

def test_find_pairs_to_reach_sum_non_int_within_list_returns_error():
    # arrange
    list = [3,5,7,"eight"]
    target_sum = 15
    # act
    result = pairs_with_given_sum(list, target_sum)
    # assert
    assert TypeError('Please give a list of integers')