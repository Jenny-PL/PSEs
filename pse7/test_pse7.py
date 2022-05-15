# from pse7 import reshape_matrix
from pse7_recursion import reshape_matrix

# example input 1: [[1,2], [3,4], [5,6], [7,8]]   #current: r= 4, c= 2
#                  r = 2, c = 4
# expected output 1: [[1, 2, 3, 4]], [5, 6, 7, 8]]

# example input 2: [[1,2],[3,4]]  #current: r =2, c =2
#                   r = 2, c = 4
# expected output 2: [[1,2], [3,4]]  # no change in matrix

def test_reshape_matrix_returns_new_matrix():
    # arrange
    matrix = [[1,2], [3,4], [5,6], [7,8]] 
    r = 2
    c =4
    # act
    result = reshape_matrix(matrix,r,c)
    # assert
    assert result ==  [[1, 2, 3, 4],[5, 6, 7, 8]]

def test_reshape_matrix_returns_input_matrix_if_not_able_to_reshape():
    # arrange 
    matrix = [[1,2],[3,4]] 
    r = 2
    c = 4
    # act
    result = reshape_matrix(matrix,r,c)
    # assert
    assert result == [[1,2],[3,4]] 