

def merge_lists(list1, list2):
    for num in list1:
        if type(num) != int:
            raise ValueError("Please give two lists of integers as input")
    for num in list2:
        if type(num) != int:
            raise ValueError("Please give two lists of integers as input")

    return sorted(list1+list2)

answer = merge_lists([1, 2, 5, 4, 5],[-2, 2, 3, 4, 7])
print(answer)