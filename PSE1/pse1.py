def get_highest_rated(restaurants):
    if restaurants == []:
        return None
    if type(restaurants) is not list:
        return "Please input a list"
    for i in range(len(restaurants)):
        if isinstance(restaurants[i]['rating'], (int, float)):
            highest_rating = max([restaurants[i]["rating"] for i in range(len(restaurants))])
        for i in range(len(restaurants)):
            if restaurants[i]['rating'] == highest_rating:
                return restaurants[i] 



a = [{"name": "Grillbys", "location": "Seattle"}]
print(get_highest_rated(a))


    

    # for i in range(len(restaurants)):
    #     if type(restaurants[i]["rating"]) != int:
    #         return "Ratings must be a single digit, 0-5"

    # ratings = [restaurants[i]["rating"] for i in range(len(restaurants))]
    # max_rating = max(ratings)
    # highest_rated_restaurants = [restaurants[i] for i in range(len(restaurants)) if restaurants[i]['rating'] == max_rating]
    # return highest_rated_restaurants

        

# example input:
# restaurants = [{"name": "Grillby's", "rating": 1}, {"name": "Crow's Nest", "rating": 5}]


# 2. Given valid input, apply logic:
#   -- Given list of dictionaries, make a list of the values associated with key 'ratings' 
#  -- Plan: Use a list comprehension, with a for loop to iterate thru dictionary, accessing values associated with key 'rating'.
# -- Use max() function to determine the highest rating (max_rating)
# -- To account for edge case of a tie in max value: use a for loop to search for other instances in which dictionary['rating'] == max_rating
# -- Once all cases of restaurants with this highest rating are identified, return dictionaries of each restaurant with max_rating