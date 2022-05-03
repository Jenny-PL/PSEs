
from pse6 import merge_lists

def test_returns_joined_sorted_list():
    # arrange
    list1 = [-30, -10, 0, 15, 16]
    list2 = [-20, -5, 5]
    # act
    result = merge_lists(list1, list2)
    # assert
    assert result == [-30, -20, -10, -5, 0, 5, 15, 16]

def test_duplicate_nums_sorted_list():
    # arrange
    list1 = [1, 2, 2, 4, 5]
    list2 = [-2, 2, 3, 4, 7]
    # act
    result = merge_lists(list1, list2)
    # assert
    assert result ==  [-2, 1, 2, 2, 2, 3, 4, 4, 5, 7]
