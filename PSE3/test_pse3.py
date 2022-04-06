from pse3 import *
from alt_pse3 import *

# example input 1:"GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT"
# expected output 1: 7

# example input 2:
# expected output 2:

def test_hamming_distance_two_equal_len_strings():
    # arrange
    dna_1 = "GAGCCTACTAACGGGAT"
    dna_2 =  "CATCGTAATGACGGCCT"

    # act
    output = hamming_distance(dna_1,dna_2)

    # assert
    assert output == 7

def test_hamming_distance_empty_strings():
    # arrange
    dna_1 = ""
    dna_2 = ""
    # act
    output = hamming_distance(dna_1,dna_2)
    # assert
    assert output is None