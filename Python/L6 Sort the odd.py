# You will be given an array of numbers. 
# You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

# Examples
# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

def sort_array(source_array):
    sorted_odds = [x for x in source_array if x%2 == 1]
    sorted_odds.sort()
    sorted_result = []
    odd = 0
    for x in source_array:
        if x%2 == 0:
            sorted_result.append(x)
        else:
            sorted_result.append(sorted_odds[odd])
            odd += 1
    return sorted_result
