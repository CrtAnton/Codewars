# Given a mixed array of number and string representations of integers, 
# add up the string integers and subtract this from the total of the non-string integers.

#Return as a number.


def div_con(x):
    return sum([int(i) for i in x if type(i) == int]) - sum([int(i) for i in x if type(i) == str])
