# Write a function that given, an array arr, returns an array containing 
# at each index i the amount of numbers that are smaller than arr[i] to the right.

# For example:

# * Input [5, 4, 3, 2, 1] => Output [4, 3, 2, 1, 0]
# * Input [1, 2, 0] => Output [1, 1, 0]

def smaller(arr):
    new = []
    for index,num in enumerate(arr):
        c= 0
        for nu in arr[index:]:
            if num>nu:
                c += 1
        new.append(c)
    return new
        
