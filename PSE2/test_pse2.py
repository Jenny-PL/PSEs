from pse2 import score, letter_dict

def test_score_simple_word():
    # arrange
    word = "word"
    # act
    output = score(word)
    # assert
    output == 8
    
def test_score_word_with_extra_characters():
    # arrange
    word = "Hello, world!"
    # act
    output = score(word)
    # assert
    output == 17