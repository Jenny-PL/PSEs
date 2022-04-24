from pse4 import is_palindrome
# example input 1: "racecar"
# expected output 1: True

# example input 2: "treehouse"
# expected output 2: False

# example input 3: "Hillih"
# expected output 3: True

# example input 4: "I"
# expected output 4: True

def test_lower_case_palindrome_returns_true():
    # arrange
    input = "racecar"
    # act
    result = is_palindrome(input)
    # assert
    assert result == True

def test_not_palindrome_returns_False():
    # arrange
    input = "treehouse"
    # act
    result = is_palindrome(input)
    # assert
    assert result == False
    
def test_palindrome_mixed_case_returns_Talse():
    # arrange
    input = "Hillih"
    # act
    result = is_palindrome(input)
    # assert
    assert result == True
    
def test_palindrome_single_letter_returns_True():
    # arrange
    input = "I"
    # act
    result = is_palindrome(input)
    # assert
    assert result == True