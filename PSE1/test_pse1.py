from pse1 import *

def test_get_highest_rated_empty_list_returns_none():
    # assign
    restaurants = []
    # act
    output = get_highest_rated(restaurants)
    # assert
    assert output == None

def test_get_highest_rated_if_input_not_list_returns_error_message():
    # assign
    restaurants = {}
    # act
    output = get_highest_rated(restaurants)
    # assert 
    assert output == "Please input a list"

# def test_get_highest_rated_if_rating_not_int_or_float_return_error_msg():
#     # assign
#     restaurants = [{"name": "Burma Super Star", "rating": "five"}, {"name": "Crow's Nest", "rating": 4}]
#     # act
#     output = get_highest_rated(restaurants)
#     # assert
#     assert output == "Ratings must be a single digit, 0-5"

def test_get_highest_rated_returns_correct_restaurant_if_no_tie():
    # assign
    restaurants = [{"name": "Burma Super Star", "rating": 5}, {"name": "Crow's Nest", "rating": 4}]
    # act
    output = get_highest_rated(restaurants)
    # assert
    assert output == [{"name": "Burma Super Star", "rating": 5}]

def test_get_highest_rated_returns_correct_restaurant_if_tie():
    # assign
    restaurants = [{"name": "Burma Super Star", "rating": 4}, {"name": "Crow's Nest", "rating": 4}, {"name": "Steve's Pizza", "rating": 3}]
    # act
    output = get_highest_rated(restaurants)
    # assert
    assert output == [{"name": "Burma Super Star", "rating": 4}, {"name": "Crow's Nest", "rating": 4}]

def test_if_name_or_rating_keys_missing_do_something_get_highest_rated():
    pass

def test_if_name_is_str_get_highest_rated():
    pass
