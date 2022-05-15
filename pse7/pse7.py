# height and width of the given matrix is in range [1, 100]. 
# The given r and c are all positive.

# [1,2], [3,4], [5,6], [7,8]
# r = 2, c = 4
# expected output 1: [[1, 2, 3, 4]], [5, 6, 7, 8]]

# helper function:
def validate_input(r,c):
    if type(r) != int and type(r) != float:
        raise ValueError("Please give positive, whole number for r and c")
    if type(c) != int and type(c) != float:
        raise ValueError("Please give positive, whole number for r and c")
    if r < 0 or c < 0:
        raise ValueError("Please give positive numbers for r and c")

def reshape_matrix(matrix,r,c):
    '''
    input: matrix: lists inside a list
    r for number of desired rows in output matrix; r is positive
    c for number of desired columns in output matrix; c is positive
    output: If desired matrix is not possible, output the input matrix;
    If desired matrix is possible, output the desired matrix
    '''
    validate_input(r,c)
    spots_needed = r * c
    all_items = []             
    for row in matrix:
        all_items.extend(row)            # space: O(n) // time: O(n) where n = r*c
    if len(all_items) > 100*100:
        raise ValueError("Please provide matrix with max height and width of 100.")
    if len(all_items) != spots_needed:
        return matrix
    else:
        new_matrix = []
        start = 0
        end = c
        for i in range(r): # number of rows desired (here r = 2, so i = 0, then 1)  # O(n) aka O(r) time complexity
            new_matrix.append(all_items[start:end])    # append has O(1) time complexity
            start += c
            end += c
        return new_matrix
            
print(reshape_matrix([[1,2],[3,4]], 4, 1))

# time complexity: O(n)
