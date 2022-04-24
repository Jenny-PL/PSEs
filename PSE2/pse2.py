letter_dict = {
    1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
    2: ["D", "G"],
    3: ["B", "C", "M", "P"],
    4: ["F", "H", "V", "W", "Y"],
    5: ["K"],
    8: ["J", "X"],
    10: ["Q", "Z"]
}

def score(word):
    word_score = 0
    for letter in word.upper():
        for letter_score, letter_list in letter_dict.items():
            if letter in letter_list:
                word_score += letter_score
    return word_score
        
    # reverse look-up example (using value to find the key):
    #     def caller_id(lookup_number):
    # for name, num in ph_directory.items():
    #     if num == lookup_number:
    #         print(name)


